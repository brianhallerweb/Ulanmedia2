//@format
import React, {Component} from 'react';
import {Redirect} from 'react-router-dom';

class GprsForEachPOffer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      authenticated: true,
      loading: false,
      dateRange: this.props.match.params.dateRange,
      gprs: [],
    };
  }

  componentDidMount() {
    this.setState({loading: true});

    fetch(`/jsonapi/createGprsForEachPOfferDataset`, {
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
          gprs: file,
          loading: false,
        });
      });
  }

  render() {
    this.state.gprs[0] &&
      console.log(
        `roi score formula \n${
          this.state.gprs[0].roi_formula
        } \n\n\ncvr score formula \n${this.state.gprs[0].cvr_formula}`,
      );
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <table style={{width: '50%'}}>
          <thead>
            <tr>
              <th>P Offer</th>
              <th>Profit</th>
              <th>GPR</th>
            </tr>
          </thead>
          <tbody>
            {this.state.gprs.map(gpr => (
              <tr key={gpr.p_offer_name}>
                <td>{gpr.p_offer_name}</td>
                <td>${gpr.p_offer_profit}</td>
                <td>{gpr.gpr}</td>
              </tr>
            ))}
          </tbody>
        </table>
        {this.state.gprs[0] && (
          <div>
            <div style={{marginTop: 20}}>
              gpr formula: {this.state.gprs[0].gpr_formula}
            </div>
            <div style={{marginTop: 20}}>
              look in console for roi score and cvr score formulas
            </div>
          </div>
        )}
      </div>
    );
  }
}

export default GprsForEachPOffer;
