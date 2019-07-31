//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import {Redirect} from 'react-router-dom';

class ListCWidgetConfirmation extends Component {
  constructor(props) {
    super(props);
    this.state = {
      authenticated: true,
      cWidgetID: this.props.match.params.cWidgetID,
      listType: this.props.match.params.listType,
      response: false,
      responseMessage: '',
    };
  }

  confirmCWidgetListing() {
    fetch(`/api/addtolist`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
        widgetID: this.state.cWidgetID,
        listType: this.state.listType,
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
          responseMessage: res,
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
          Are you sure you want to list c widget {this.state.cWidgetID} as{' '}
          {this.state.listType}?
        </p>
        <div>
          <button onClick={() => this.confirmCWidgetListing()}>
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

export default ListCWidgetConfirmation;
