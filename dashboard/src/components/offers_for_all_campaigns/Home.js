//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import Title from './Title';
import NavBar from './NavBar';
import Records from './Records';
import GlobalNavBar from '../GlobalNavBar';
import {Redirect} from 'react-router-dom';
import checkForMismatchVolWeightAndRecWeight from './checkForMismatchVolWeightAndRecWeight';
import checkForBadOffers from './checkForBadOffers';
import InternalLink from '../utilities/InternalLink';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      dateRange: 'oneeighty',
      volRequestStartDate: '',
      volRequestEndDate: '',
      volRequestDates: '',
      mismatchVolWeightAndRecWeightCount: 0,
      badOffersCount: 0,
      c1: false,
      c1Value: 'good',
      c2: false,
      c2Value: 20,
      c3: false,
      c3Value: 50,
      c4: false,
      c4Value: 0,
      c5: false,
      error: false,
      authenticated: true,
      loading: false,
      offersRecords: [],
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

    fetch(`/jsonapi/createOffersForAllCampaignsDataset`, {
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
          volRequestDates: `${file.metadata.vol_start_date} to ${
            file.metadata.vol_end_date
          }`,
        });
      })
      .then(() =>
        fetch('/jsonapi/createOffersForAllCampaignsReport', {
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
            c1: this.state.c1,
            c2: this.state.c2,
            c3: this.state.c3,
            c4: this.state.c4,
            c5: this.state.c5,
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
        let mismatchVolWeightAndRecWeightCount = checkForMismatchVolWeightAndRecWeight(
          records,
        );
        let badOffersCount = checkForBadOffers(records);

        let error;
        records.length ? (error = false) : (error = true);
        this.setState({
          offersRecords: records,
          mismatchVolWeightAndRecWeightCount,
          badOffersCount,
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
        <Title volRequestDates={this.state.volRequestDates} />
        <GlobalNavBar />
        <div style={{marginBottom: 10}}>
          <a
            style={{fontSize: 12}}
            href="https://drive.google.com/file/d/1KdfVFWD-2lQze6IMUUO36IaiboSsz2md/view?usp=sharing"
            target="_blank">
            flowchart
          </a>
        </div>
        <div style={{marginBottom: 10, fontSize: 12}}>
          <InternalLink
            className={'rowLink'}
            stopPropagation={true}
            to={`/gprsforeachpoffer/${this.state.dateRange}`}
            target={'_blank'}
            label={'View the gpr for each p offer'}
          />
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
          submitForm={this.submitForm.bind(this)}
          loading={this.state.loading}
        />

        {this.state.mismatchVolWeightAndRecWeightCount !== 0 &&
          !this.state.loading && (
            <div style={{color: 'red', marginTop: 10}}>
              {this.state.mismatchVolWeightAndRecWeightCount} offers with
              mismatched voluum weight and recommended weight
            </div>
          )}
        {this.state.badOffersCount !== 0 && !this.state.loading && (
          <div style={{color: 'red', marginTop: 10}}>
            {this.state.badOffersCount} bad offers
          </div>
        )}

        <Records
          error={this.state.error}
          loading={this.state.loading}
          offersRecords={this.state.offersRecords}
          volRequestStartDate={this.state.volRequestStartDate}
          volRequestEndDate={this.state.volRequestEndDate}
        />
      </div>
    );
  }
}

export default Home;
