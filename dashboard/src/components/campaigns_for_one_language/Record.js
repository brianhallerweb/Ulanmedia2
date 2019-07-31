//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import InternalLink from '../utilities/InternalLink';

class Record extends Component {
  constructor(props) {
    super(props);
    this.campaignID = this.props.language.campaign_id;
    this.campaignName = this.props.language.campaign_name;
    this.clicks = this.props.language.clicks;
    this.cost = this.props.language.cost;
    this.revenue = this.props.language.revenue;
    this.profit = this.props.language.profit;
    this.conversions = this.props.language.conversions;
    this.cvr = this.props.language.cvr;
    this.epc = this.props.language.epc;
    this.cpa = this.props.language.cpa;
    this.cpc = this.props.language.cpc;
    this.epa = this.props.language.epa;
    this.roi = this.props.language.roi;
    this.state = {clicked: false, hovered: false};
  }

  outlineRow(hovered, classification) {
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
                to={`/languagesforonecampaign/${this.campaignID}/${
                  this.campaignName
                }/`}
                target={'_blank'}
                label={'languages'}
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
        <td>{this.conversions}</td>
        <td>${this.cpa}</td>
        <td>${this.epa}</td>
        <td>{this.cvr}%</td>
        <td>{this.roi}%</td>
      </tr>
    );
  }
}

export default Record;
