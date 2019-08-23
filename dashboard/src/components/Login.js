//@format
import React, {Component} from 'react';
import {Redirect} from 'react-router-dom';

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: '',
      error: false,
      tokenAcquired: false,
    };
  }

  submitForm() {
    const username = this.state.username.trim();
    const password = this.state.password.trim();
    fetch(`/jsonapi/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username,
        password,
      }),
    })
      .then(res => {
        if (!res.ok) {
          this.setState({error: true, password: ''});
          throw Error(res.statusText);
        }
        return res.json();
      })
      .then(res => {
        console.log(res);
        localStorage.setItem('access_token', res.access_token);
        localStorage.setItem('refresh_token', res.refresh_token);
        this.setState({tokenAcquired: true});
      })
      .catch(err => console.log(err));
  }

  render() {
    return (
      <div style={{margin: 40}}>
        <h3 style={{paddingLeft: 5}}>Ulan Media 2 Dashboard</h3>
        <form
          onSubmit={e => {
            e.preventDefault();
            this.submitForm();
          }}>
          <div style={{padding: 5}}>
            <input
              type="text"
              placeholder="username"
              value={this.state.username}
              onChange={e => {
                this.setState({username: e.target.value});
              }}
            />
          </div>
          <div style={{padding: 5}}>
            <input
              type="password"
              placeholder="password"
              value={this.state.password}
              onChange={e => {
                this.setState({password: e.target.value});
              }}
            />
          </div>
          <div style={{padding: 5}}>
            <input type="submit" value="Submit" />
          </div>
        </form>
        {this.state.tokenAcquired && (
          <Redirect to={this.props.location.location || '/'} />
        )}
        {this.state.error && <p style={{color: 'red'}}>incorrect login</p>}
      </div>
    );
  }
}

export default Login;
