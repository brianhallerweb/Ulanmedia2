//@format
import React, {Component} from 'react';
import Logout from './Logout';
import {Redirect} from 'react-router-dom';

class UpdateAllData extends Component {
  constructor(props) {
    super(props);
    this.state = {
      authenticated: true,
      loading: false,
    };
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <Logout />
        <p>Are you sure you want to update all data?</p>
        <div>
          <button onClick={() => this.setState({loading: true})}>
            <a href="http://scripts.brianhaller.net">Yes</a>
          </button>
        </div>
        {this.state.loading && <div className="loader" />}
      </div>
    );
  }
}

export default UpdateAllData;
