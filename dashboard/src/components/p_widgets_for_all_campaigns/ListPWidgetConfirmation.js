//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import {Redirect} from 'react-router-dom';
import {Link} from 'react-router-dom';

class ListPWidgetConfirmation extends Component {
  constructor(props) {
    super(props);
    this.state = {
      authenticated: true,
      pWidgetID: this.props.match.params.pWidgetID,
      listType: this.props.match.params.listType,
      response: false,
      responseMessage: '',
    };
  }

  confirmPWidgetListing() {
    fetch(`/jsonapi/colorlist/${this.state.listType}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        widget_id: this.state.pWidgetID,
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
      .then(res =>
        this.setState({
          response: true,
          responseMessage: res.message,
        }),
      )
      .catch(err => {
        console.log(err);
      });
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <Logout />
        <p>
          Are you sure you want to list p widget {this.state.pWidgetID} as{' '}
          {this.state.listType}?
        </p>
        {this.state.listType == 'grey' && (
          <div style={{marginTop: 10, marginBottom: 15}}>
            Remember to exclude the widget in bad campaigns
          </div>
        )}
        {this.state.listType == 'black' && (
          <div style={{marginTop: 10, marginBottom: 15}}>
            {'Remember to '}
            <Link
              to={{
                pathname: `/excludepwidgetconfirmation/${this.state.pWidgetID}`,
              }}
              target="_blank">
              exclude
            </Link>
            {' the widget in all campaigns'}
          </div>
        )}
        <div>
          <button onClick={() => this.confirmPWidgetListing()}>
            Yes, confirm listing
          </button>
        </div>
        {this.state.response && (
          <div>
            <p style={{color: 'green'}}>{this.state.responseMessage}</p>
            <div style={{marginTop: 10}}>
              <button onClick={() => close()}>close tab</button>
            </div>
          </div>
        )}
      </div>
    );
  }
}

export default ListPWidgetConfirmation;
