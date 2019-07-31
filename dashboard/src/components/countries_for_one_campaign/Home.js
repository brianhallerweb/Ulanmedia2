//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import Title from './Title';
import NavBar from './NavBar';
import Records from './Records';
import GlobalNavBar from '../GlobalNavBar';
import {Redirect} from 'react-router-dom';
import checkForBadCountries from './checkForBadCountries';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      dateRange: 'oneeighty',
      campaignID: this.props.match.params.volid,
      campaignName: this.props.match.params.name,
      volRequestDates: '',
      badCountriesCount: 0,
      c1: false,
      c1Value: 'good',
      c2: false,
      c2Value: 20,
      c3: false,
      c3Value: 50,
      error: false,
      authenticated: true,
      loading: false,
      countriesRecords: [],
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

    fetch(`/jsonapi/createCountriesForOneCampaignDataset`, {
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
        fetch('/jsonapi/createCountriesForOneCampaignReport', {
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
        let badCountriesCount = checkForBadCountries(records);

        let error;
        records.length ? (error = false) : (error = true);
        this.setState({
          countriesRecords: records,
          badCountriesCount,

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
            href="https://drive.google.com/file/d/1vFmrY0MUj5icKWEoutheTe-n33GUmY4d/view?usp=sharing"
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
        {this.state.badCountriesCount !== 0 && !this.state.loading && (
          <div style={{color: 'red', marginTop: 10}}>
            {this.state.badCountriesCount} countries are bad
          </div>
        )}

        <Records
          error={this.state.error}
          loading={this.state.loading}
          countriesRecords={this.state.countriesRecords}
        />
      </div>
    );
  }
}

export default Home;
