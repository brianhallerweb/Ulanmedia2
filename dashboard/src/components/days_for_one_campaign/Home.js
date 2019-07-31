//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import Title from './Title';
import Records from './Records';
import GlobalNavBar from '../GlobalNavBar';
import {Redirect} from 'react-router-dom';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      campaignID: this.props.match.params.widgetID,
      dayRecords: [],
      loading: false,
      authenticated: true,
    };
  }

  componentDidMount() {
    this.setState({loading: true});
    fetch('/jsonapi/createDaysForOneCampaignReport', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
        volid: this.props.match.params.volid,
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
      .then(dayRecords => {
        this.setState({dayRecords, loading: false});
      })
      .catch(err => console.log(err));
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <Logout />
        <Title dayRecords={this.state.dayRecords} />
        <GlobalNavBar />
        <div style={{marginBottom: 10}}>
          *Remember the Cost, Profit, Clicks, CPC, CPL, Lead CVR, CPS, and ROI
          are not highly accurate, they're just estimates based on Voluum's
          daily averaged CPC evenly distributed across received
          clicks....instead of being based on MGID's variable CPC actual charged
          clicks.
        </div>

        <Records
          loading={this.state.loading}
          dayRecords={this.state.dayRecords}
        />
      </div>
    );
  }
}

export default Home;
