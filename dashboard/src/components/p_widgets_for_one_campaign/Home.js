//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import Title from './Title';
import NavBar from './NavBar';
import Records from './Records';
import GlobalNavBar from '../GlobalNavBar';
import {Redirect} from 'react-router-dom';
import checkForBadAndIncludedPWidgets from './checkForBadAndIncludedPWidgets';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      volid: this.props.match.params.volid,
      name: this.props.match.params.name,
      widgetRecords: [],
      mgidRequestDates: '',
      volRequestDates: '',
      dateRange: 'oneeighty',
      error: false,
      authenticated: true,
      loading: false,
      badAndIncludedPWidgetsCount: 0,
      c1: false,
      c1Value: 'wait',
      c2: false,
      c2Value: 'included',
      c3: false,
      c3Value: 'waiting',
      c4: false,
      c4Value: 10,
      c5: false,
      c5Value: 10,
      c6: false,
      c6Value: 0,
      c7: false,
      c7Value: 0,
      c8: false,
      c9: true,
      c9Value: 0.5,
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

    fetch(`/jsonapi/createPWidgetsForOneCampaignDataset`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
        volID: this.state.volid,
        dateRange: this.state.dateRange,
        maxRecBid: this.state.c9Value,
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
          mgidRequestDates: `${file.metadata.mgid_start_date} to ${
            file.metadata.mgid_end_date
          }`,
          volRequestDates: `${file.metadata.vol_start_date} to ${
            file.metadata.vol_end_date
          }`,
        });
      })
      .then(() =>
        fetch('/jsonapi/createPWidgetsForOneCampaignReport', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'x-auth': localStorage.getItem('token'),
          },
          body: JSON.stringify({
            dateRange: this.state.dateRange,
            volID: this.state.volid,
            c1Value: this.state.c1Value,
            c2Value: this.state.c2Value,
            c3Value: this.state.c3Value,
            c4Value: this.state.c4Value,
            c5Value: this.state.c5Value,
            c6Value: this.state.c6Value,
            c7Value: this.state.c7Value,
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
        let badAndIncludedPWidgetsCount = checkForBadAndIncludedPWidgets(
          records,
        );
        let error;
        records.length ? (error = false) : (error = true);
        this.setState({
          widgetRecords: records,
          badAndIncludedPWidgetsCount,
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
          name={this.props.match.params.name}
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
          datasetsCreated={this.state.datasetsCreated}
          selectDateRange={this.selectDateRange.bind(this)}
          setConditionValue={this.setConditionValue.bind(this)}
          toggleCondition={this.toggleCondition.bind(this)}
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
          c7Value={this.state.c7Value}
          c8={this.state.c8}
          c9={this.state.c9}
          c9Value={this.state.c9Value}
          submitForm={this.submitForm.bind(this)}
          loading={this.state.loading}
          maxLeadCPA={this.props.match.params.max_lead_cpa}
        />
        {this.state.badAndIncludedPWidgetsCount !== 0 &&
          !this.state.loading && (
            <div style={{color: 'red', marginTop: 10}}>
              {this.state.badAndIncludedPWidgetsCount} p widgets need to be
              excluded from the campaign
            </div>
          )}

        <Records
          loading={this.state.loading}
          error={this.state.error}
          widgetRecords={this.state.widgetRecords}
          name={this.state.name}
        />
      </div>
    );
  }
}

export default Home;
