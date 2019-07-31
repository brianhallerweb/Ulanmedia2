//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import Title from './Title';
import NavBar from './NavBar';
import Records from './Records';
import GlobalNavBar from '../GlobalNavBar';
import {Redirect} from 'react-router-dom';
import checkForBadLanguages from './checkForBadLanguages';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      dateRange: 'oneeighty',
      campaignID: this.props.match.params.volid,
      campaignName: this.props.match.params.name,
      volRequestDates: '',
      badLanguagesCount: 0,
      c1: false,
      c1Value: 'good',
      c2: false,
      c2Value: 20,
      c3: false,
      c3Value: 50,
      error: false,
      authenticated: true,
      loading: false,
      languagesRecords: [],
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
    this.setState({loading: true, volRequestDates: ''});

    fetch(`/jsonapi/createLanguagesForOneCampaignDataset`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
        dateRange: this.state.dateRange,
        campaignID: this.state.campaignID,
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
        fetch('/jsonapi/createLanguagesForOneCampaignReport', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'x-auth': localStorage.getItem('token'),
          },
          body: JSON.stringify({
            dateRange: this.state.dateRange,
            campaignID: this.state.campaignID,
            c1Value: this.state.c1Value,
            c2Value: this.state.c2Value,
            c3Value: this.state.c3Value,
            c1: this.state.c1,
            c2: this.state.c2,
            c3: this.state.c3,
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
        let badLanguagesCount = checkForBadLanguages(records);

        let error;
        records.length ? (error = false) : (error = true);
        this.setState({
          languagesRecords: records,
          badLanguagesCount,
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
          volRequestDates={this.state.volRequestDates}
          campaignName={this.state.campaignName}
        />
        <GlobalNavBar />
        <div style={{marginBottom: 10}}>
          <a
            style={{fontSize: 12}}
            href="https://drive.google.com/file/d/1GobH3SpPoG3ZBnidbBQ2uRXaBgjm6DQI/view"
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
          submitForm={this.submitForm.bind(this)}
          loading={this.state.loading}
        />
        {this.state.badLanguagesCount !== 0 && !this.state.loading && (
          <div style={{color: 'red', marginTop: 10}}>
            {this.state.badLanguagesCount} languages are bad
          </div>
        )}

        <Records
          error={this.state.error}
          loading={this.state.loading}
          languagesRecords={this.state.languagesRecords}
        />
      </div>
    );
  }
}

export default Home;
