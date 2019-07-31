//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import InternalLink from '../utilities/InternalLink';
import ExternalLink from '../utilities/ExternalLink';

class Record extends Component {
  constructor(props) {
    super(props);
    this.mgid_id = this.props.campaign.mgid_id;
    this.vol_id = this.props.campaign.vol_id;
    this.name = this.props.campaign.name;
    this.classification = this.props.campaign.classification;
    this.clicks = this.props.campaign.clicks;
    this.cost = this.props.campaign.cost;
    this.revenue = this.props.campaign.revenue;
    this.profit = this.props.campaign.profit;
    this.leads = this.props.campaign.leads;
    this.mpl = this.props.campaign.mpl;
    this.sales = this.props.campaign.sales;
    this.cps = this.props.campaign.cps;
    this.mps = this.props.campaign.mps;
    this.cpc = this.props.campaign.cpc;
    this.epc = this.props.campaign.epc;
    this.cpl = this.props.campaign.cpl;
    this.epl = this.props.campaign.epl;
    this.eps = this.props.campaign.eps;
    this.mpc = this.props.campaign.mpc;
    //////////////////////////////////
    /////////////////////////////////
    // mgid and voluum urls
    this.mgidURL = `https://dashboard.mgid.com/advertisers/edit/campaign_id/${
      this.mgid_id
    }`;

    this.deviceOSBrowserURL = `
https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_d8393dfa-ef8c-444e-8880-7b2e0e118cf5/report/device,os,browser?dateRange=custom-date&sortKey=visits&sortDirection=desc&page=1&chart=0&columns=deviceName&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=1000&reportType=&include=ACTIVE&reportDataType=0&tagsGrouping=device&valueFiltersGrouping=device&from=${
      this.props.volRequestStartDate
    }T00:00:00Z&to=${
      this.props.volRequestEndDate
    }T00:00:00Z&filter1=campaign&filter1Value=${this.vol_id}

`;

    this.ISPURL = `
https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_ef605826-ad4d-458c-8a01-855e5a0f0601/report/isp?dateRange=custom-date&chart=0&columns=deviceName&columns=os&columns=browser&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&limit=1000&reportType=tree&include=ACTIVE&reportDataType=0&tagsGrouping=device&valueFiltersGrouping=device&from=${
      this.props.volRequestStartDate
    }T00:00:00Z&to=${
      this.props.volRequestEndDate
    }T00:00:00Z&filter1=campaign&filter1Value=${this.vol_id}

`;

    this.monthsURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_d8393dfa-ef8c-444e-8880-7b2e0e118cf5/report/month?dateRange=custom-date&sortKey=month&sortDirection=asc&page=1&chart=0&columns=month&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=1000&reportType=&include=ACTIVE&reportDataType=0&tagsGrouping=month&valueFiltersGrouping=month&from=${
      this.props.volRequestStartDate
    }T00:00:00Z&to=${
      this.props.volRequestEndDate
    }T00:00:00Z&filter1=campaign&filter1Value=${this.vol_id}`;

    ////////////////////////////

    this.state = {clicked: false, hovered: false};
  }

  // 2/10/19 I disabled the tool tips because they are totally out of date and
  // not being used at this time.
  //createTooltip(profit, maxSaleCPA, clicks, leads, cost, maxLeadCPA, leadCPA) {
  //const textArr = [];
  //if (clicks > 1000 && leads == 0) {
  //textArr.push(
  //`Campaign has more than 1000 clicks (${clicks}) but no leads (${leads}) --- (clicks > 1000 AND leads = 0)`,
  //);
  //}
  //if (cost > 0.25 * maxSaleCPA && leadCPA > 3 * maxLeadCPA) {
  //textArr.push(
  //`Campaign cost (\$${cost}) is more than a quarter of maxSaleCPA (\$${0.25 *
  //maxSaleCPA}) AND leadCPA (\$${leadCPA}) is more than 3x maxLeadCPA (\$${3 *
  //maxLeadCPA}) --- (cost > 0.25*maxSaleCPA AND leadCPA > 3*maxLeadCPA)`,
  //);
  //}
  //if (cost > 0.3 * maxSaleCPA && leadCPA > 2 * maxLeadCPA) {
  //textArr.push(
  //`Campaign cost (\$${cost}) is more than a third of maxSaleCPA (\$${0.3 *
  //maxSaleCPA}) AND leadCPA (\$${leadCPA}) is more than 2x maxLeadCPA (\$${2 *
  //maxLeadCPA}) --- (cost > 0.3*maxSaleCPA AND leadCPA > 2*maxLeadCPA)`,
  //);
  //}
  //if (cost > 0.5 * maxSaleCPA && leadCPA > 1.5 * maxLeadCPA) {
  //textArr.push(
  //`Campaign cost (\$${cost}) is more than half of maxSaleCPA (\$${0.5 *
  //maxSaleCPA}) AND leadCPA (\$${leadCPA}) is more than 1.5x maxLeadCPA (\$${1.5 *
  //maxLeadCPA}) --- (cost > 0.5*maxSaleCPA AND leadCPA > 1.5*maxLeadCPA)`,
  //);
  //}
  //if (cost > 2 * maxSaleCPA && leadCPA > maxLeadCPA) {
  //textArr.push(
  //`Campaign cost (\$${cost}) is more than 2x maxSaleCPA (\$${2 *
  //maxSaleCPA}) AND leadCPA (\$${leadCPA}) is more than maxLeadCPA (\$${maxLeadCPA}) --- (cost > 2*maxSaleCPA AND leadCPA > maxLeadCPA)`,
  //);
  //}

  //let toolTipText = `Campaign lost ${(-profit / maxSaleCPA).toFixed(
  //2,
  //)}x of maxSaleCPA (\$${-profit})\n
  //`;
  //for (let i = 0; i < textArr.length; i++) {
  //toolTipText += `\u2022 ${textArr[i]}\n`;
  //}
  //return toolTipText;
  //}

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
    } else if (classification === 'wait') {
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
          {/*<td className="tooltip">*/}
          {this.name}
          {/*
	    <span className="tooltiptext">
            {
	      this.createTooltip(
	      this.profit,
	      this.max_sale_cpa,
	      this.clicks,
	      this.leads,
	      this.cost,
	      this.max_lead_cpa,
	      this.lead_cpa,)
            }

          </span>
	   */}
          <div>
            <ExternalLink
              className={'rowLink'}
              href={this.mgidURL}
              target={'_blank'}
              label={'mgid'}
            />

            <InternalLink
              className={'rowLink'}
              stopPropagation={true}
              to={`/pwidgetsforonecampaign/${this.vol_id}/${this.name}/`}
              target={'_blank'}
              label={'p_widgets'}
            />

            <InternalLink
              className={'rowLink'}
              stopPropagation={true}
              to={`/cwidgetsforonecampaign/${this.vol_id}/${this.name}/`}
              target={'_blank'}
              label={'c_widgets'}
            />

            <InternalLink
              className={'rowLink'}
              stopPropagation={true}
              to={`/offersforonecampaign/${this.vol_id}/${this.name}/`}
              target={'_blank'}
              label={'offers'}
            />

            <InternalLink
              className={'rowLink'}
              stopPropagation={true}
              to={`/adsforonecampaign/${this.vol_id}/${this.name}/`}
              target={'_blank'}
              label={'ads'}
            />

            <InternalLink
              className={'rowLink'}
              stopPropagation={true}
              to={`/countriesforonecampaign/${this.vol_id}/${this.name}/`}
              target={'_blank'}
              label={'countries'}
            />

            <InternalLink
              className={'rowLink'}
              stopPropagation={true}
              to={`/languagesforonecampaign/${this.vol_id}/${this.name}/`}
              target={'_blank'}
              label={'languages'}
            />

            <ExternalLink
              className={'rowLink'}
              href={this.deviceOSBrowserURL}
              target={'_blank'}
              label={'device/os/browser'}
            />

            <ExternalLink
              className={'rowLink'}
              href={this.ISPURL}
              target={'_blank'}
              label={'isp'}
            />

            <ExternalLink
              className={'rowLink'}
              href={this.monthsURL}
              target={'_blank'}
              label={'months'}
            />

            <InternalLink
              className={'rowLink'}
              stopPropagation={true}
              to={`/daysforonecampaign/${this.vol_id}/`}
              target={'_blank'}
              label={'days'}
            />
          </div>
        </td>
        {this.stylizeClassificationText(this.classification)}
        <td>${this.cost}</td>
        <td>${this.revenue}</td>
        <td>${this.profit}</td>
        <td>{this.clicks}</td>
        <td>${this.cpc}</td>
        <td>${this.epc}</td>
        <td>${this.mpc}</td>
        <td>{this.leads}</td>
        <td>${this.cpl}</td>
        <td>${this.epl}</td>
        <td>${this.mpl}</td>
        <td>{this.sales}</td>
        <td>${this.cps}</td>
        <td>${this.eps}</td>
        <td>${this.mps}</td>
      </tr>
    );
  }
}

export default Record;
