//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import Title from './Title';
import NavBar from './NavBar';
import Records from './Records';
import GlobalNavBar from '../GlobalNavBar';
import {Redirect} from 'react-router-dom';
import {Link} from 'react-router-dom';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      campaignRecords: [],
      dateRange: 'oneeighty',
      error: false,
      authenticated: true,
      loading: false,
      c1: true,
      c1Value: 0.5,
      c2: true,
      c2Value: 2,
      c3: false,
      c3Value: 10,
    };
  }

  componentDidMount() {
    this.submitForm();
  }

  selectDateRange(dateRange) {
    this.setState({dateRange: dateRange});
  }

  toggleCondition(condition) {
    this.setState({[condition]: !this.state[condition]});
  }

  setConditionValue(condition, conditionValue) {
    this.setState({[condition]: conditionValue});
  }

  submitForm() {
    this.setState({
      loading: true,
    });

    fetch(`/jsonapi/createCampaignsForGoodPWidgetsDataset`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
        dateRange: this.state.dateRange,
        maxRecBid: this.state.c1Value,
        defaultCoeff: this.state.c2Value,
      }),
    })
      .then(res => {
        if (!res.ok) {
          if (res.status == 401) {
            //the case when a token is in the browser but it doesn't
            //match what it is in the database. This can happen when the
            //token is manipulated in the browser or if the tokens are
            //deleted from the database without the user logging out.
            localStorage.removeItem('token');
            this.setState({authenticated: false});
          }
          throw Error(res.statusText);
        }
        return res;
      })
      .then(res => res.json())
      .then(file => {})
      .then(() =>
        fetch(`/jsonapi/createCampaignsForGoodPWidgetsReport`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'x-auth': localStorage.getItem('token'),
          },
          body: JSON.stringify({
            dateRange: this.state.dateRange,
            c3Value: this.state.c3Value,
            c3: this.state.c3,
          }),
        }),
      )
      .then(res => res.json())
      .then(records => {
        let error;
        records.length ? (error = false) : (error = true);
        this.setState({
          campaignRecords: records,
          error,
          loading: false,
        });
      })
      .catch(err => console.log(err));
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <Logout />
        <Title />
        <GlobalNavBar />
        <NavBar
          dateRange={this.state.dateRange}
          selectDateRange={this.selectDateRange.bind(this)}
          toggleCondition={this.toggleCondition.bind(this)}
          setConditionValue={this.setConditionValue.bind(this)}
          c1={this.state.c1}
          c1Value={this.state.c1Value}
          c2={this.state.c2}
          c2Value={this.state.c2Value}
          c3={this.state.c3}
          c3Value={this.state.c3Value}
          loading={this.state.loading}
          submitForm={this.submitForm.bind(this)}
        />
        <Records
          error={this.state.error}
          loading={this.state.loading}
          campaignRecords={this.state.campaignRecords}
        />
      </div>
    );
  }
}

export default Home;
