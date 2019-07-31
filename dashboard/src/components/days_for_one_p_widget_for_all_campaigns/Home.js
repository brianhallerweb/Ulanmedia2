//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import Title from './Title';
import Links from './Links';
import Records from './Records';
import GlobalNavBar from '../GlobalNavBar';
import {Redirect} from 'react-router-dom';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      pWidgetID: this.props.match.params.pWidgetID,
      volRequestDates: '',
      dayRecords: [],
      loading: false,
      authenticated: true,
      error: false,
    };
  }

  componentDidMount() {
    this.setState({loading: true});

    fetch('/jsonapi/createDaysForOnePWidgetForAllCampaignsDataset', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
        pWidgetID: this.state.pWidgetID,
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
      .then(file => {
        this.setState({
          volRequestDates: `${file.metadata.vol_start_date} to ${
            file.metadata.vol_end_date
          }`,
        });
      })
      .then(() =>
        fetch('/jsonapi/createDaysForOnePWidgetForAllCampaignsReport', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'x-auth': localStorage.getItem('token'),
          },
          body: JSON.stringify({
            pWidgetID: this.state.pWidgetID,
          }),
        }),
      )
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
      .then(records => {
        let error;
        records.length ? (error = false) : (error = true);
        this.setState({
          dayRecords: records,
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
        <Title
          pWidgetID={this.state.pWidgetID}
          volRequestDates={this.state.volRequestDates}
        />
        <GlobalNavBar />
        <div style={{marginBottom: 10}}>
          *Remember the Cost, Clicks, Profit, CPC, CPL, Lead CVR, CPS, and ROI
          are not highly accurate, they're just estimates based on Voluum's
          daily averaged CPC evenly distributed across received
          clicks....instead of being based on MGID's variable CPC actual charged
          clicks.
        </div>
        <Links pWidgetID={this.state.pWidgetID} />
        <Records
          error={this.state.error}
          loading={this.state.loading}
          dayRecords={this.state.dayRecords}
        />
      </div>
    );
  }
}

export default Home;
