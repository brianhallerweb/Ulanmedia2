//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import Title from './Title';
import Widgets from './Widgets';
import AddWidget from './AddWidget';
import GlobalNavBar from '../GlobalNavBar';
import {Redirect} from 'react-router-dom';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      color: 'white',
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
        Authorization: `Bearer ${localStorage.getItem('access_token')}`,
      },
    })
      .then(res => {
        if (!res.ok) {
          if (res.status == 401) {
            localStorage.removeItem('access_token');
            this.setState({authenticated: false});
          }
        }
        return res;
      })
      .then(res => res.json())
      .then(list => {
        this.setState({widgets: list[`color_widgets_and_domains`]});
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
            Authorization: `Bearer ${localStorage.getItem('access_token')}`,
          },
          body: JSON.stringify({
            widget_id: widget,
          }),
        })
          .then(res => {
            if (!res.ok) {
              if (res.status == 401) {
                localStorage.removeItem('access_token');
                this.setState({authenticated: false});
              }
            }
            return res;
          })
          .then(res => res.json())
          .then(res => {
            if (res['success_message']) {
              successes.push(res['success_message']);
            }
            if (res['error_message']) {
              errors.push(res['error_message']);
            }
          })
          .then(() =>
            fetch(`/jsonapi/complete${this.state.color}list`, {
              method: 'GET',
              headers: {
                Authorization: `Bearer ${localStorage.getItem('access_token')}`,
              },
            }),
          )
          .then(res => {
            if (!res.ok) {
              if (res.status == 401) {
                localStorage.removeItem('access_token');
                this.setState({authenticated: false});
              }
            }
            return res;
          })
          .then(res => res.json())
          .then(list => {
            this.setState({
              widgets: list[`color_widgets_and_domains`],
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
        Authorization: `Bearer ${localStorage.getItem('access_token')}`,
      },
      body: JSON.stringify({
        widget_id: widget,
      }),
    })
      .then(res => {
        if (!res.ok) {
          if (res.status == 401) {
            localStorage.removeItem('access_token');
            this.setState({authenticated: false});
          }
        }
        return res;
      })
      .then(res => res.json())
      .then(res => {
        if (res['success_message']) {
          successes.push(res['success_message']);
        }

        if (res['error_message']) {
          errors.push(res['error_message']);
        }
      })
      .then(() =>
        fetch(`/jsonapi/complete${this.state.color}list`, {
          method: 'GET',
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access_token')}`,
          },
        }),
      )
      .then(res => {
        if (!res.ok) {
          if (res.status == 401) {
            localStorage.removeItem('access_token');
            this.setState({authenticated: false});
          }
        }
        return res;
      })
      .then(res => res.json())
      .then(list => {
        this.setState({
          widgets: list[`color_widgets_and_domains`],
          successes,
          errors,
        });
      });
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <GlobalNavBar />
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
