//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import {Redirect} from 'react-router-dom';
import {Link} from 'react-router-dom';

class ExcludePWidgetConfirmation extends Component {
  constructor(props) {
    super(props);
    this.state = {
      authenticated: true,
      campaigns: [],
      pWidgetID: this.props.match.params.pWidgetID,
      loading: false,
    };
  }

  componentDidMount() {
    this.getCampaigns();
  }

  getCampaigns() {
    fetch(`/api/readcampaignsets`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
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
        return res.json();
      })
      .then(campaigns => this.setState({campaigns}))
      .catch(err => console.log(err));
  }

  excludeOneCampaign(pWidgetID, mgidCampaignID) {
    return new Promise((resolve, reject) => {
      fetch(`/api/excludecampaignforoneporcwidget`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-auth': localStorage.getItem('token'),
        },
        body: JSON.stringify({
          pWidgetID,
          mgidCampaignID,
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
          return res.json();
        })
        .then(res => {
          resolve(res);
        })
        .catch(err => reject(err));
    });
  }

  //excludeAllCampaigns is the important function on this page. It is what
  //excludes each campaign from a p widget, one by one.
  async excludeAllCampaigns() {
    // This function is async because I wanted to slow down the requests
    // to mgid. It excludes each campaign, one at a time.
    this.setState({loading: true});
    for (let campaign of this.state.campaigns) {
      //exclude one campaign and then update the list of excluded p
      //widgets for that campaign
      const excluded = await this.excludeOneCampaign(
        this.state.pWidgetID,
        campaign.mgid_id,
      );

      if (excluded.id) {
        console.log(
          `campaign ${campaign.mgid_id} successfully excluded from p widget ${
            this.state.pWidgetID
          }`,
        );
      } else {
        console.log(
          `ERROR: campaign ${campaign.mgid_id} failed to be excluded from ${
            this.state.pWidgetID
          }. The specific error is on the next line. `,
        );
        console.log(excluded);
      }
    }

    this.setState({loading: false});
    console.log('END OF EXCLUDE SCRIPT');
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <Logout />
        <p>
          Are you sure you want to exclude all campaigns from p widget{' '}
          {this.state.pWidgetID}?
        </p>

        <div style={{marginTop: 10, marginBottom: 15}}>
          {'Remember to add the widget to the '}
          <Link
            to={{
              pathname: `/listpwidgetconfirmation/${
                this.state.pWidgetID
              }/black`,
            }}
            target="_blank">
            blacklist
          </Link>
        </div>

        <div>
          <button
            disabled={!this.state.campaigns.length > 0}
            onClick={() => this.excludeAllCampaigns()}>
            Yes, confirm exclusion
          </button>
        </div>
        <p style={{fontSize: 12}}>
          Look in browser console for feedback (ctrl+shift+j)
        </p>
        {this.state.loading && (
          <div style={{margin: 10}}>
            <div className="loader" />
            <div>This will take a 5-10 minutes...</div>
          </div>
        )}
      </div>
    );
  }
}

export default ExcludePWidgetConfirmation;
