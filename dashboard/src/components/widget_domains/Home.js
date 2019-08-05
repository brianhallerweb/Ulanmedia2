//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import Title from './Title';
import WidgetDomains from './WidgetDomains';
import AddWidgetDomain from './AddWidgetDomain';
import {Redirect} from 'react-router-dom';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      widgetDomains: [],
      authenticated: true,
      successes: [],
      errors: [],
    };
  }

  componentDidMount() {
    fetch(`/jsonapi/completewidgetdomains`, {
      method: 'GET',
      headers: {
        Authorization: `JWT ${localStorage.getItem('token')}`,
      },
    })
      .then(res => res.json())
      .then(widgetDomains => {
        this.setState({widgetDomains: widgetDomains['widget domains']});
      });
  }

  handleAdd(input) {
    const successes = [];
    const errors = [];

    if (!input) {
      errors.push('no widget domains entered');
      return this.setState({successes, errors});
    }

    const widgetDomains = input.split('\n');
    for (let widgetDomain of widgetDomains) {
      if (widgetDomain === '') {
        continue;
      }

      const entireWidgetDomain = widgetDomain.split(',');
      if (entireWidgetDomain.length !== 3) {
        continue;
      }
      const trafficSource = entireWidgetDomain[0].trim();
      const widgetID = entireWidgetDomain[1].trim();
      const domain = entireWidgetDomain[2].trim();

      fetch(`/jsonapi/widgetdomain`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `JWT ${localStorage.getItem('token')}`,
        },
        body: JSON.stringify({
          traffic_source: trafficSource,
          widget_id: widgetID,
          domain: domain,
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
          fetch(`/jsonapi/completewidgetdomains`, {
            method: 'GET',
            headers: {
              Authorization: `JWT ${localStorage.getItem('token')}`,
            },
          }),
        )
        .then(res => res.json())
        .then(widgetDomains => {
          this.setState({
            widgetDomains: widgetDomains['widget domains'],
            successes,
            errors,
          });
        })
        .catch(err => console.log(err));
    }
  }

  handleDelete(trafficSource, widgetID, domain) {
    const successes = [];
    const errors = [];

    fetch(`/jsonapi/widgetdomain`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `JWT ${localStorage.getItem('token')}`,
      },
      body: JSON.stringify({
        traffic_source: trafficSource,
        widget_id: widgetID,
        domain: domain,
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
        fetch(`/jsonapi/completewidgetdomains`, {
          method: 'GET',
          headers: {
            Authorization: `JWT ${localStorage.getItem('token')}`,
          },
        }),
      )
      .then(res => res.json())
      .then(widgetDomains => {
        this.setState({
          widgetDomains: widgetDomains['widget domains'],
          successes,
          errors,
        });
      })
      .catch(err => console.log(err));
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
        <AddWidgetDomain handleAdd={this.handleAdd.bind(this)} />

        <WidgetDomains
          widgetDomains={this.state.widgetDomains}
          handleDelete={this.handleDelete.bind(this)}
        />
      </div>
    );
  }
}

export default Home;
