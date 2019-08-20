//@format
import React, {Component} from 'react';
import {Redirect} from 'react-router-dom';
import GlobalNavBar from './GlobalNavBar';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div style={{margin: 40}}>
        <GlobalNavBar />
      </div>
    );
  }
}

export default Home;
