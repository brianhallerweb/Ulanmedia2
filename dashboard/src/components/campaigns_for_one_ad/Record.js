//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import InternalLink from '../utilities/InternalLink';

class Record extends Component {
  constructor(props) {
    super(props);
    this.name = this.props.campaign.name;
    this.volID = this.props.campaign.vol_id;
    this.cost = this.props.campaign.cost;
    this.revenue = this.props.campaign.revenue;
    this.profit = this.props.campaign.profit;
    this.clicks = this.props.campaign.clicks;
    this.ctr = this.props.campaign.ctr;
    this.cpc = this.props.campaign.cpc;
    this.epc = this.props.campaign.epc;
    this.leads = this.props.campaign.leads;
    this.cpl = this.props.campaign.cpl;
    this.epl = this.props.campaign.epl;
    this.lead_cvr = this.props.campaign.lead_cvr;
    this.sales = this.props.campaign.sales;
    this.cps = this.props.campaign.cps;
    this.eps = this.props.campaign.eps;
    this.roi = this.props.campaign.roi;
    this.imps = this.props.campaign.imps;
    this.ppi = this.props.campaign.ppi;
    this.state = {clicked: false, hovered: false};
  }

  addRowLinks() {
    return (
      <div>
        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/adsforonecampaign/${this.volID}/${this.name}/`}
          target={'_blank'}
          label={'ads'}
        />
        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/monthsforoneadforonecampaign/${this.props.adImage}/${
            this.volID
          }/${this.name}/`}
          target={'_blank'}
          label={'months'}
        />

        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/daysforoneadforonecampaign/${this.props.adImage}/${
            this.volID
          }/${this.name}/`}
          target={'_blank'}
          label={'days'}
        />
      </div>
    );
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
          {this.name}
          {this.name !== 'summary' && this.addRowLinks()}
        </td>
        <td>${this.cost}</td>
        <td>${this.revenue}</td>
        <td>${this.profit}</td>
        <td>{this.imps}</td>
        <td>${this.ppi}</td>
        <td>{this.clicks}</td>
        <td>{this.ctr}%</td>
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
