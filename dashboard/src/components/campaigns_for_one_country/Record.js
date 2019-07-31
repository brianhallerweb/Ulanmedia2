//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import InternalLink from '../utilities/InternalLink';

class Record extends Component {
  constructor(props) {
    super(props);
    this.campaignID = this.props.country.campaign_id;
    this.campaignName = this.props.country.campaign_name;
    this.cost = this.props.country.cost;
    this.revenue = this.props.country.revenue;
    this.profit = this.props.country.profit;
    this.clicks = this.props.country.clicks;
    this.cpc = this.props.country.cpc;
    this.epc = this.props.country.epc;
    this.leads = this.props.country.leads;
    this.cpl = this.props.country.cpl;
    this.epl = this.props.country.epl;
    this.lead_cvr = this.props.country.lead_cvr;
    this.sales = this.props.country.sales;
    this.cps = this.props.country.cps;
    this.eps = this.props.country.eps;
    this.roi = this.props.country.roi;
    this.state = {};
  }
  outlineRow(hovered) {
    if (hovered) {
      return 'black';
    } else {
      return 'transparent';
    }
  }

  render() {
    return (
      <tr
        style={{
          outlineStyle: 'solid',
          outlineColor: this.outlineRow(this.state.hovered),
        }}
        className={this.state.clicked && 'clicked'}
        onMouseEnter={e => {
          this.setState({hovered: !this.state.hovered});
        }}
        onMouseLeave={e => {
          this.setState({hovered: !this.state.hovered});
        }}
        onClick={e => {
          this.setState({clicked: !this.state.clicked});
        }}>
        <td>
          {this.campaignName}
          {this.campaignName !== 'summary' && (
            <div>
              <InternalLink
                className={'rowLink'}
                stopPropagation={true}
                to={`/countriesforonecampaign/${this.campaignID}/${
                  this.campaignName
                }/`}
                target={'_blank'}
                label={'countries'}
              />
            </div>
          )}
        </td>
        <td>${this.cost}</td>
        <td>${this.revenue}</td>
        <td>${this.profit}</td>
        <td>{this.clicks}</td>
        <td>${this.cpc}</td>
        <td>${this.epc}</td>
        <td>{this.leads}</td>
        <td>${this.cpl}</td>
        <td>${this.epl}</td>
        <td>{this.lead_cvr}%</td>
        <td>{this.sales}</td>
        <td>${this.cps}</td>
        <td>${this.eps}</td>
        <td>{this.roi}%</td>
      </tr>
    );
  }
}

export default Record;
