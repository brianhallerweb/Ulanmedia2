//@format
import React, {Component} from 'react';
import Logout from './Logout';
import {Redirect} from 'react-router-dom';

class UpdateOneEightyData extends Component {
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
        <p>Are you sure you want to update the data for 180 days?</p>
        <div>
          <button onClick={() => this.setState({loading: true})}>
            <a href="http://scripts.brianhaller.net/updateoneeighty.php">Yes</a>
          </button>
        </div>
        {this.state.loading && <div className="loader" />}
      </div>
    );
  }
}

export default UpdateOneEightyData;
