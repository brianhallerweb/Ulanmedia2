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
      widgets: [],
      authenticated: true,
      successes: [],
      errors: [],
    };
  }

  componentDidMount() {
    fetch(`/jsonapi/completegoodwidgets`)
      .then(res => res.json())
      .then(widgets => {
        this.setState({widgets: widgets['good widgets']});
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
        fetch(`/jsonapi/goodwidget`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
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
          .then(() => fetch(`/jsonapi/completegoodwidgets`))
          .then(res => res.json())
          .then(widgets => {
            this.setState({
              widgets: widgets['good widgets'],
              successes,
              errors,
            });
          })
          .catch(err => console.log(err));
      }
    }
  }

  handleDelete(widget) {
    const successes = [];
    const errors = [];

    fetch(`/jsonapi/goodwidget`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
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
      .then(() => fetch(`/jsonapi/completegoodwidgets`))
      .then(res => res.json())
      .then(widgets => {
        this.setState({widgets: widgets['good widgets'], successes, errors});
      });
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <Title />
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
