//@format
import React, {Component} from 'react';
import {Redirect} from 'react-router-dom';

class Logout extends Component {
  constructor(props) {
    super(props);
    this.state = {
      tokenRemoved: false,
    };
  }

  logout() {
    fetch('/api/users/logout', {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
    })
      .then(res => {
        if (!res.ok) {
          throw Error(res.statusText);
        }
        return res;
      })
      .then(res => {
        localStorage.removeItem('token');
        this.setState({tokenRemoved: true});
      })
      .catch(err => console.log(err));
  }

  render() {
    return (
      <div style={{float: 'right'}}>
        <button
          style={{fontSize: 10, marginBottom: 5}}
          onClick={this.logout.bind(this)}>
          logout
        </button>
      </div>
    );
  }
}

export default Logout;
