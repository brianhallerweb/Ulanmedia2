//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import InternalLink from '../utilities/InternalLink';
import ExternalLink from '../utilities/ExternalLink';

class Record extends Component {
  constructor(props) {
    super(props);
    this.offerID = this.props.offer.offer_id;
    this.flowRule = this.props.offer.flow_rule;
    this.volWeight = this.props.offer.vol_weight;
    this.recWeight = this.props.offer.rec_weight;
    this.classification = this.props.offer.classification;
    this.roiScore = this.props.offer.roi_score;
    this.gpr = this.props.offer.gpr;
    this.cvrScore = this.props.offer.cvr_score;
    this.totalScore = this.props.offer.total_score;
    this.offerName = this.props.offer.offer_name;
    this.cost = this.props.offer.cost;
    this.revenue = this.props.offer.revenue;
    this.profit = this.props.offer.profit;
    this.clicks = this.props.offer.clicks;
    this.cpc = this.props.offer.cpc;
    this.epc = this.props.offer.epc;
    this.leads = this.props.offer.leads;
    this.cpl = this.props.offer.cpl;
    this.epl = this.props.offer.epl;
    this.lead_cvr = this.props.offer.lead_cvr;
    this.sales = this.props.offer.sales;
    this.cps = this.props.offer.cps;
    this.eps = this.props.offer.eps;
    this.roi = this.props.offer.roi;
    this.hasMismatchVolWeightAndRecWeight = this.props.offer.has_mismatch_vol_weight_and_rec_weight;
    // link urls
    this.widgetsURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_eb062435-2077-4a1b-a48f-fdf3468aa823/report/custom-variable-1?dateRange=last-30-days&sortKey=visits&sortDirection=desc&page=1&chart=0&columns=customVariable1&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=1000&reportType=&include=ALL&reportDataType=0&tagsGrouping=custom-variable-1&valueFiltersGrouping=custom-variable-1&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc&filter2=offer&filter2Value=${
      this.offerID
    }`;
    this.adsURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_9b2776aa-e86d-4b85-9f72-742aac32a505/report/custom-variable-5?dateRange=last-30-days&sortKey=visits&sortDirection=desc&page=1&chart=0&columns=customVariable5&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=1000&reportType=&include=ALL&reportDataType=0&tagsGrouping=custom-variable-5&valueFiltersGrouping=custom-variable-5&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc&filter2=offer&filter2Value=${
      this.offerID
    }`;
    this.countriesURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_eb062435-2077-4a1b-a48f-fdf3468aa823/report/country-code?dateRange=custom-date&sortKey=visits&sortDirection=desc&page=1&chart=0&columns=countryName&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=1000&reportType=&include=ACTIVE&reportDataType=0&tagsGrouping=country-code&valueFiltersGrouping=country-code&from=${
      this.props.volRequestStartDate
    }T00:00:00Z&to=${
      this.props.volRequestEndDate
    }T00:00:00Z&filter1=offer&filter1Value=${this.offerID}`;

    this.languagesURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_eb062435-2077-4a1b-a48f-fdf3468aa823/report/language?dateRange=custom-date&sortKey=visits&sortDirection=desc&page=1&chart=0&columns=languageName&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=1000&reportType=&include=ACTIVE&reportDataType=0&tagsGrouping=language&valueFiltersGrouping=language&from=${
      this.props.volRequestStartDate
    }T00:00:00Z&to=${
      this.props.volRequestEndDate
    }T00:00:00Z&filter1=offer&filter1Value=${this.offerID}`;

    this.deviceOSBrowserURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_eb062435-2077-4a1b-a48f-fdf3468aa823/report/device,os,browser?dateRange=custom-date&sortKey=visits&sortDirection=desc&page=1&chart=0&columns=deviceName&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=1000&reportType=&include=ALL&reportDataType=0&tagsGrouping=device&valueFiltersGrouping=device&from=${
      this.props.volRequestStartDate
    }T00:00:00Z&to=${
      this.props.volRequestEndDate
    }T00:00:00Z&filter1=offer&filter1Value=${this.offerID}`;

    this.ISPURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_b6851828-574a-44d8-a496-353edfbce0be/report/isp?dateRange=custom-date&sortKey=visits&sortDirection=desc&page=1&chart=0&columns=isp&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=1000&reportType=tree&include=ALL&reportDataType=0&tagsGrouping=isp&valueFiltersGrouping=isp&from=${
      this.props.volRequestStartDate
    }T00:00:00Z&to=${
      this.props.volRequestEndDate
    }T00:00:00Z&filter1=offer&filter1Value=${this.offerID}`;

    /////////////////

    this.state = {clicked: false, hovered: false};
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

  outlineRow(hovered, hasMismatchVolWeightAndRecWeight) {
    if (hasMismatchVolWeightAndRecWeight) {
      return 'red';
    } else if (hovered) {
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
          outlineColor: this.outlineRow(
            this.state.hovered,
            this.hasMismatchVolWeightAndRecWeight,
          ),
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
          {this.offerName}
          <div>
            <InternalLink
              className={'rowLink'}
              stopPropagation={true}
              to={`/campaignsforoneoffer/${this.offerID}/${this.offerName}`}
              target={'_blank'}
              label={'campaigns'}
            />

            <ExternalLink
              className={'rowLink'}
              href={this.widgetsURL}
              target={'_blank'}
              label={'widgets'}
            />

            <ExternalLink
              className={'rowLink'}
              href={this.adsURL}
              target={'_blank'}
              label={'ads'}
            />

            <ExternalLink
              className={'rowLink'}
              href={this.countriesURL}
              target={'_blank'}
              label={'countries'}
            />

            <ExternalLink
              className={'rowLink'}
              href={this.languagesURL}
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

            <InternalLink
              className={'rowLink'}
              stopPropagation={true}
              to={`/monthsforoneofferforallcampaigns/${this.offerName}`}
              target={'_blank'}
              label={'months'}
            />

            <InternalLink
              className={'rowLink'}
              stopPropagation={true}
              to={`/daysforoneofferforallcampaigns/${this.offerName}`}
              target={'_blank'}
              label={'days'}
            />
          </div>
        </td>
        <td>
          {this.flowRule}
          <div>
            <InternalLink
              className={'rowLink'}
              stopPropagation={true}
              to={`/offersforoneflowrule/${this.flowRule}/
                  `}
              target={'_blank'}
              label={'offers'}
            />
          </div>
        </td>
        <td>{this.classification}</td>
        <td>
          {this.roiScore} + {this.cvrScore} + {this.gpr} = {this.totalScore}
        </td>
        <td>{this.volWeight}</td>
        <td>{this.recWeight}</td>
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
