//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import Title from './Title';
import CampaignSets from './CampaignSets';
import AddCampaignSet from './AddCampaignSet';
import {Redirect} from 'react-router-dom';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      campaignSets: [],
      authenticated: true,
      successes: [],
      errors: [],
    };
  }

  componentDidMount() {
    fetch(`/jsonapi/completecampaignsets`, {
      method: 'GET',
      headers: {
        Authorization: `JWT ${localStorage.getItem('token')}`,
      },
    })
      .then(res => res.json())
      .then(campaignSets => {
        this.setState({campaignSets: campaignSets['campaign sets']});
      });
  }

  handleAdd(campaignSet) {
    const successes = [];
    const errors = [];
    if (
      campaignSet.volCampaignID === '' ||
      campaignSet.mgidCampaignID === '' ||
      campaignSet.campaignName === '' ||
      campaignSet.maxLeadCPA === '' ||
      campaignSet.maxSaleCPA === '' ||
      campaignSet.campaignStatus === ''
    ) {
      errors.push('incomplete campaign set');
      return this.setState({successes, errors});
    }

    fetch(`/jsonapi/campaignset`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `JWT ${localStorage.getItem('token')}`,
      },
      body: JSON.stringify({
        vol_campaign_id: campaignSet.volCampaignID,
        mgid_campaign_id: campaignSet.mgidCampaignID,
        campaign_name: campaignSet.campaignName,
        max_lead_cpa: campaignSet.maxLeadCPA,
        max_sale_cpa: campaignSet.maxSaleCPA,
        campaign_status: campaignSet.campaignStatus,
      }),
    })
      .then(res => res.json())
      .then(res => {
        if (res['success message']) {
          successes.push(res['success message']);
        }

        if (res['error message']) {
          errors.push(res['error message']);
        }
      })
      .then(() =>
        fetch(`/jsonapi/completecampaignsets`, {
          method: 'GET',
          headers: {
            Authorization: `JWT ${localStorage.getItem('token')}`,
          },
        }),
      )
      .then(res => res.json())
      .then(campaignSets => {
        this.setState({
          campaignSets: campaignSets['campaign sets'],
          successes,
          errors,
        });
      })
      .catch(err => console.log(err));
  }

  handleDelete(volCampaignID) {
    const successes = [];
    const errors = [];

    fetch(`/jsonapi/campaignset`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `JWT ${localStorage.getItem('token')}`,
      },
      body: JSON.stringify({
        vol_campaign_id: volCampaignID,
      }),
    })
      .then(res => res.json())
      .then(res => {
        if (res['success message']) {
          successes.push(res['success message']);
        }

        if (res['error message']) {
          errors.push(res['error message']);
        }
      })
      .then(() =>
        fetch(`/jsonapi/completecampaignsets`, {
          method: 'GET',
          headers: {
            Authorization: `JWT ${localStorage.getItem('token')}`,
          },
        }),
      )
      .then(res => res.json())
      .then(campaignSets => {
        this.setState({
          campaignSets: campaignSets['campaign sets'],
          successes,
          errors,
        });
      });
  }

  handleRowUpdate(index, key, value) {
    const updatedCampaignSets = this.state.campaignSets;
    updatedCampaignSets[index][key] = value;
    this.setState({campaignSets: updatedCampaignSets});
  }

  handleUpdateCampaignSet(campaignSet) {
    const successes = [];
    const errors = [];
    fetch(`/jsonapi/campaignset`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `JWT ${localStorage.getItem('token')}`,
      },
      body: JSON.stringify({
        vol_campaign_id: campaignSet.volCampaignID,
        mgid_campaign_id: campaignSet.mgidCampaignID,
        campaign_name: campaignSet.campaignName,
        max_lead_cpa: campaignSet.maxLeadCPA,
        max_sale_cpa: campaignSet.maxSaleCPA,
        campaign_status: campaignSet.campaignStatus,
      }),
    })
      .then(res => res.json())
      .then(res => {
        if (res['success message']) {
          successes.push(res['success message']);
        }

        if (res['error message']) {
          errors.push(res['error message']);
        }
      })
      .then(() =>
        fetch(`/jsonapi/completecampaignsets`, {
          method: 'GET',
          headers: {
            Authorization: `JWT ${localStorage.getItem('token')}`,
          },
        }),
      )
      .then(res => res.json())
      .then(campaignSets => {
        this.setState({
          campaignSets: campaignSets['campaign sets'],
          successes,
          errors,
        });
      })
      .catch(err => console.log(err));
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <Title />
        {this.state.successes.length > 0 &&
          this.state.successes.map(success => (
            <div
              style={{marginTop: 5, marginBottom: 15, color: 'green'}}
              key={success}>
              {success}
            </div>
          ))}
        {this.state.errors.length > 0 &&
          this.state.errors.map(error => (
            <div
              style={{marginTop: 5, marginBottom: 15, color: 'red'}}
              key={error}>
              {error}
            </div>
          ))}
        <AddCampaignSet handleAdd={this.handleAdd.bind(this)} />
        <CampaignSets
          campaignSets={this.state.campaignSets}
          handleDelete={this.handleDelete.bind(this)}
          handleRowUpdate={this.handleRowUpdate.bind(this)}
          handleUpdateCampaignSet={this.handleUpdateCampaignSet.bind(this)}
        />
      </div>
    );
  }
}

export default Home;
