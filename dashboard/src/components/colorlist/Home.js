//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import Title from './Title';
import Widgets from './Widgets';
import AddWidget from './AddWidget';
import {Redirect} from 'react-router-dom';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      color: this.props.match.params.color,
      widgets: [],
      authenticated: true,
      successes: [],
      errors: [],
    };
  }

  componentDidMount() {
    fetch(`/jsonapi/complete${this.state.color}list`, {
      method: 'GET',
      headers: {
        Authorization: `JWT ${localStorage.getItem('token')}`,
      },
    })
      .then(res => res.json())
      .then(list => {
        this.setState({widgets: list[`${this.state.color}list`]});
      });
  }

  handleAdd(widget) {
    const successes = [];
    const errors = [];

    if (!widget) {
      errors.push('no widget entered');
      return this.setState({successes, errors});
    }

    const widgets = widget.split(',');
    for (let widget of widgets) {
      widget = widget.trim();
      if (widget) {
        fetch(`/jsonapi/${this.state.color}list`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `JWT ${localStorage.getItem('token')}`,
          },
          body: JSON.stringify({
            widget_id: widget,
          }),
        })
          .then(res => res.json())
          .then(res => {
            if (res['success message']) {
              successes.push(res['success message']);
            }
            if (res['error message']) {
              errors.push(res['error message']);
            }
          })
          .then(() =>
            fetch(`/jsonapi/complete${this.state.color}list`, {
              method: 'GET',
              headers: {
                Authorization: `JWT ${localStorage.getItem('token')}`,
              },
            }),
          )
          .then(res => res.json())
          .then(list => {
            this.setState({
              widgets: list[`${this.state.color}list`],
              successes,
              errors,
            });
          });
      }
    }
  }

  handleDelete(widget) {
    const successes = [];
    const errors = [];

    fetch(`/jsonapi/${this.state.color}list`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `JWT ${localStorage.getItem('token')}`,
      },
      body: JSON.stringify({
        widget_id: widget,
      }),
    })
      .then(res => res.json())
      .then(res => {
        if (res['success message']) {
          successes.push(res['success message']);
        }

        if (res['error message']) {
          errors.push(res['error message']);
        }
      })
      .then(() =>
        fetch(`/jsonapi/complete${this.state.color}list`, {
          method: 'GET',
          headers: {
            Authorization: `JWT ${localStorage.getItem('token')}`,
          },
        }),
      )
      .then(res => res.json())
      .then(list => {
        this.setState({
          widgets: list[`${this.state.color}list`],
          successes,
          errors,
        });
      });
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <Title color={this.state.color} />
        {this.state.successes.length > 0 &&
          this.state.successes.map(success => (
            <div
              style={{marginTop: 5, marginBottom: 15, color: 'green'}}
              key={success}>
              {success}
            </div>
          ))}
        {this.state.errors.length > 0 &&
          this.state.errors.map(error => (
            <div
              style={{marginTop: 5, marginBottom: 15, color: 'red'}}
              key={error}>
              {error}
            </div>
          ))}
        <AddWidget handleAdd={this.handleAdd.bind(this)} />
        <Widgets
          widgets={this.state.widgets}
          handleDelete={this.handleDelete.bind(this)}
        />
      </div>
    );
  }
}

export default Home;
