//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import InternalLink from '../utilities/InternalLink';

class Record extends Component {
  constructor(props) {
    super(props);
    this.image = this.props.ad.image;
    this.classification = this.props.ad.classification;
    this.cost = this.props.ad.cost;
    this.revenue = this.props.ad.revenue;
    this.profit = this.props.ad.profit;
    this.clicks = this.props.ad.clicks;
    this.ctr = this.props.ad.ctr;
    this.cpc = this.props.ad.cpc;
    this.epc = this.props.ad.epc;
    this.leads = this.props.ad.leads;
    this.cpl = this.props.ad.cpl;
    this.epl = this.props.ad.epl;
    this.lead_cvr = this.props.ad.lead_cvr;
    this.sales = this.props.ad.sales;
    this.cps = this.props.ad.cps;
    this.eps = this.props.ad.eps;
    this.roi = this.props.ad.roi;
    this.imps = this.props.ad.imps;
    this.ctr = this.props.ad.ctr;
    this.ppi = this.props.ad.ppi;
    this.localRank = this.props.ad.local_rank;
    this.localRankOrder = this.props.ad.local_rank_order;
    this.finalRank = this.props.ad.final_rank;
    this.finalRankOrder = this.props.ad.final_rank_order;
    this.globalRank = this.props.ad.global_rank;
    this.globalRankOrder = this.props.ad.global_rank_order;
    this.state = {clicked: false, hovered: false};
  }
  addRowLinks() {
    return (
      <div>
        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/campaignsforonead/${this.image}/`}
          target={'_blank'}
          label={'campaigns'}
        />

        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/monthsforoneadforonecampaign/${this.image}/${
            this.props.volID
          }/${this.props.name}/`}
          target={'_blank'}
          label={'months'}
        />

        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/daysforoneadforonecampaign/${this.image}/${this.props.volID}/${
            this.props.name
          }/`}
          target={'_blank'}
          label={'days'}
        />
      </div>
    );
  }

  stylizeClassificationText(row) {
    if ((row === 'bad') | (row === 'half bad')) {
      return <td style={{color: 'red', fontWeight: 900}}>{row}</td>;
    } else if ((row === 'good') | (row === 'half good')) {
      return <td style={{color: 'green', fontWeight: 900}}>{row}</td>;
    } else {
      return <td>{row}</td>;
    }
  }

  colorizeRow(classification) {
    if (classification === 'good') {
      //green
      return '#eafcea';
    } else if (classification === 'half good') {
      //light green
      return '#edfcea';
    } else if (classification === 'bad') {
      //red
      return '#f7d9d9';
    } else if (classification === 'half bad') {
      //light red
      return '#f7d9e1';
    } else if (classification === 'not yet') {
      //light grey
      return '#fafafa';
    }
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
          backgroundColor: this.colorizeRow(this.classification),
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
          {this.image}
          {this.image !== 'summary' && this.addRowLinks()}
        </td>
        <td>
          {this.globalRankOrder} ({this.globalRank})
        </td>
        <td>
          {this.localRankOrder} ({this.localRank})
        </td>
        <td>
          {this.finalRankOrder} ({this.finalRank})
        </td>
        {this.stylizeClassificationText(this.classification)}
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
