//@format
import React, {Component} from 'react';
import {Redirect} from 'react-router-dom';

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      email: '',
      password: '',
      error: false,
      tokenAcquired: false,
    };
  }

  submitForm() {
    const email = this.state.email.trim();
    const password = this.state.password.trim();
    fetch('/api/users/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email,
        password,
      }),
    })
      .then(res => {
        if (!res.ok) {
          this.setState({error: true, password: ''});
          throw Error(res.statusText);
        }
        return res;
      })
      .then(res => {
        localStorage.setItem('token', res.headers.get('x-auth'));
        this.setState({tokenAcquired: true});
      })
      .catch(err => console.log(err));
  }

  render() {
    return (
      <div style={{margin: 40}}>
        <h3 style={{paddingLeft: 5}}>Ulan Media Dashboard</h3>
        <form
          onSubmit={e => {
            e.preventDefault();
            this.submitForm();
          }}>
          <div style={{padding: 5}}>
            <input
              type="text"
              placeholder="email"
              value={this.state.email}
              onChange={e => {
                this.setState({email: e.target.value});
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
