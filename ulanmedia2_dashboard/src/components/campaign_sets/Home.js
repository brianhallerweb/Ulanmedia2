//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import Title from './Title';
import CampaignSets from './CampaignSets';
import AddCampaignSet from './AddCampaignSet';
import GlobalNavBar from '../GlobalNavBar';
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
    this.getCompleteCampaignSets();
  }

  getCompleteCampaignSets() {
    const access_token = localStorage.getItem('access_token');

    fetch(`/jsonapi/completecampaignsets`, {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${access_token}`,
      },
    })
      .then(res => {
        if (!res.ok) {
          if (res.status == 401) {
            localStorage.removeItem('access_token');
            this.setState({authenticated: false});
          }
        }

        return res;
      })
      .then(res => res.json())
      .then(campaignSets => {
        this.setState({campaignSets: campaignSets['campaign_sets']});
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
        Authorization: `Bearer ${localStorage.getItem('access_token')}`,
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
      .then(res => {
        if (!res.ok) {
          if (res.status == 401) {
            localStorage.removeItem('access_token');
            this.setState({authenticated: false});
          }
        }
        return res;
      })
      .then(res => res.json())
      .then(res => {
        if (res['success_message']) {
          successes.push(res['success_message']);
        }

        if (res['error_message']) {
          errors.push(res['error_message']);
        }
      })
      .then(() =>
        fetch(`/jsonapi/completecampaignsets`, {
          method: 'GET',
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access_token')}`,
          },
        }),
      )
      .then(res => {
        if (!res.ok) {
          if (res.status == 401) {
            localStorage.removeItem('access_token');
            this.setState({authenticated: false});
          }
        }
        return res;
      })
      .then(res => res.json())
      .then(campaignSets => {
        this.setState({
          campaignSets: campaignSets['campaign_sets'],
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
        Authorization: `Bearer ${localStorage.getItem('access_token')}`,
      },
      body: JSON.stringify({
        vol_campaign_id: volCampaignID,
      }),
    })
      .then(res => {
        if (!res.ok) {
          if (res.status == 401) {
            localStorage.removeItem('access_token');
            this.setState({authenticated: false});
          }
        }
        return res;
      })
      .then(res => res.json())
      .then(res => {
        if (res['success_message']) {
          successes.push(res['success_message']);
        }

        if (res['error message']) {
          errors.push(res['error_message']);
        }
      })
      .then(() =>
        fetch(`/jsonapi/completecampaignsets`, {
          method: 'GET',
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access_token')}`,
          },
        }),
      )
      .then(res => {
        if (!res.ok) {
          if (res.status == 401) {
            localStorage.removeItem('access_token');
            this.setState({authenticated: false});
          }
        }
        return res;
      })
      .then(res => res.json())
      .then(campaignSets => {
        this.setState({
          campaignSets: campaignSets['campaign_sets'],
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
        Authorization: `Bearer ${localStorage.getItem('access_token')}`,
      },
      body: JSON.stringify({
        vol_campaign_id: campaignSet.vol_campaign_id,
        mgid_campaign_id: campaignSet.mgid_campaign_id,
        campaign_name: campaignSet.campaign_name,
        max_lead_cpa: campaignSet.max_lead_cpa,
        max_sale_cpa: campaignSet.max_sale_cpa,
        campaign_status: campaignSet.campaign_status,
      }),
    })
      .then(res => {
        if (!res.ok) {
          if (res.status == 401) {
            localStorage.removeItem('token');
          }
          throw Error(res.statusText);
        }
        return res;
      })
      .then(res => res.json())
      .then(res => {
        if (res['success_message']) {
          successes.push(res['success_message']);
        }

        if (res['error_message']) {
          errors.push(res['error_message']);
        }
      })
      .then(() =>
        fetch(`/jsonapi/completecampaignsets`, {
          method: 'GET',
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access_token')}`,
          },
        }),
      )
      .then(res => {
        if (!res.ok) {
          if (res.status == 401) {
            localStorage.removeItem('access_token');
          }
        }
        return res;
      })
      .then(res => res.json())
      .then(campaignSets => {
        this.setState({
          campaignSets: campaignSets['campaign_sets'],
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
        <GlobalNavBar />
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
