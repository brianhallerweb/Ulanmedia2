//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import InternalLink from '../utilities/InternalLink';

class Record extends Component {
  constructor(props) {
    super(props);
    this.campaignName = this.props.campaign.campaign_name;
    this.volID = this.props.campaign.campaign_id;
    this.cost = this.props.campaign.cost;
    this.revenue = this.props.campaign.revenue;
    this.profit = this.props.campaign.profit;
    this.clicks = this.props.campaign.clicks;
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
          {this.campaignName != 'summary' && (
            <div>
              <InternalLink
                className={'rowLink'}
                stopPropagation={true}
                to={`/offersforonecampaign/${this.volID}/${this.campaignName}/`}
                target={'_blank'}
                label={'offers'}
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
