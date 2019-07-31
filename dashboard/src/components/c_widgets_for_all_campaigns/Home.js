//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import Title from './Title';
import NavBar from './NavBar';
import Records from './Records';
import GlobalNavBar from '../GlobalNavBar';
import {Redirect} from 'react-router-dom';
import checkForMismatchClassificationAndGlobalStatus from './checkForMismatchClassificationAndGlobalStatus';
import checkForBadAndIncludedCampaigns from './checkForBadAndIncludedCampaigns';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      widgetRecords: [],
      dateRange: 'oneeighty',
      volRequestStartDate: '',
      volRequestEndDate: '',
      mgidRequestDates: '',
      volRequestDates: '',
      error: false,
      authenticated: true,
      loading: false,
      mismatchClassificationAndGlobalStatusCount: 0,
      hasBadAndIncludedCampaignsCount: 0,
      c1: false,
      c1Value: 'wait',
      c2: false,
      c2Value: 'waiting',
      c3: true,
      c3Value: 10,
      c4: false,
      c4Value: 10,
      c5: false,
      c5Value: 10,
      c6: false,
      c6Value: 2,
      c7: true,
      c8: false,
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
    this.setState({loading: true, mgidRequestDates: '', volRequestDates: ''});

    fetch('/jsonapi/createCWidgetsForAllCampaignsDataset', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
        dateRange: this.state.dateRange,
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
          volRequestStartDate: file.metadata.vol_start_date,
          volRequestEndDate: file.metadata.vol_end_date,
          mgidRequestDates: `${file.metadata.mgid_start_date} to ${
            file.metadata.mgid_end_date
          }`,
          volRequestDates: `${file.metadata.vol_start_date} to ${
            file.metadata.vol_end_date
          }`,
        });
      })
      .then(() =>
        fetch('/jsonapi/createCWidgetsForAllCampaignsReport', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'x-auth': localStorage.getItem('token'),
          },
          body: JSON.stringify({
            dateRange: this.state.dateRange,
            c1Value: this.state.c1Value,
            c2Value: this.state.c2Value,
            c3Value: this.state.c3Value,
            c4Value: this.state.c4Value,
            c5Value: this.state.c5Value,
            c6Value: this.state.c6Value,
            c1: this.state.c1,
            c2: this.state.c2,
            c3: this.state.c3,
            c4: this.state.c4,
            c5: this.state.c5,
            c6: this.state.c6,
            c7: this.state.c7,
            c8: this.state.c8,
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
        let mismatchClassificationAndGlobalStatusCount = checkForMismatchClassificationAndGlobalStatus(
          records,
        );
        let hasBadAndIncludedCampaignsCount = checkForBadAndIncludedCampaigns(
          records,
        );
        let error;
        records.length ? (error = false) : (error = true);
        this.setState({
          widgetRecords: records,
          mismatchClassificationAndGlobalStatusCount,
          hasBadAndIncludedCampaignsCount,
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
          mgidRequestDates={this.state.mgidRequestDates}
          volRequestDates={this.state.volRequestDates}
        />
        <GlobalNavBar />
        <div style={{marginBottom: 10}}>
          <a
            style={{fontSize: 12}}
            href="https://drive.google.com/file/d/1lTcfx6Vm72_NBLBkRFteKFbR9rxXhDbS/view?usp=sharing"
            target="_blank">
            flowchart
          </a>
        </div>
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
          c4={this.state.c4}
          c4Value={this.state.c4Value}
          c5={this.state.c5}
          c5Value={this.state.c5Value}
          c6={this.state.c6}
          c6Value={this.state.c6Value}
          c7={this.state.c7}
          c8={this.state.c8}
          submitForm={this.submitForm.bind(this)}
          loading={this.state.loading}
        />
        {this.state.mismatchClassificationAndGlobalStatusCount !== 0 &&
          !this.state.loading && (
            <div style={{color: 'red', marginTop: 10}}>
              {this.state.mismatchClassificationAndGlobalStatusCount} widgets
              with mismatched classification and global status
            </div>
          )}
        {this.state.hasBadAndIncludedCampaignsCount !== 0 &&
          !this.state.loading && (
            <div style={{color: 'red', marginTop: 10}}>
              {this.state.hasBadAndIncludedCampaignsCount} widgets have bad and
              included campaigns
            </div>
          )}
        <Records
          error={this.state.error}
          loading={this.state.loading}
          widgetRecords={this.state.widgetRecords}
          volRequestStartDate={this.state.volRequestStartDate}
          volRequestEndDate={this.state.volRequestEndDate}
        />
      </div>
    );
  }
}

export default Home;
