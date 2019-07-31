//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import InternalLink from '../utilities/InternalLink';
import ExternalLink from '../utilities/ExternalLink';

class Record extends Component {
  constructor(props) {
    super(props);

    this.countriesURL = `h
ttps://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_9a96a80f-83fd-4721-b245-5d2d82077632/report/country-code?dateRange=last-30-days&sortKey=visits&sortDirection=desc&page=1&chart=0&columns=countryName&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=100&reportType=table&include=ACTIVE&reportDataType=0&tagsGrouping=country-code&valueFiltersGrouping=country-code&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc&filter2=custom-variable-1&filter2Value=${
      this.props.widgetRecord.widget_id
    }`;

    this.languagesURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_b311a56b-7d18-4d38-bde7-9d27d1a3eb1f/report/language?dateRange=last-30-days&sortKey=visits&sortDirection=desc&page=1&chart=0&columns=countryName&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=100&reportType=table&include=ACTIVE&reportDataType=0&tagsGrouping=language&valueFiltersGrouping=language&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc&filter2=custom-variable-1&filter2Value=${
      this.props.widgetRecord.widget_id
    }`;

    this.deviceOSURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_5a5a89b9-b146-4fb6-9ea4-128f8e675251/report/custom-variable-1,device,os?dateRange=last-30-days&sortKey=profit&sortDirection=asc&page=1&chart=0&columns=customVariable1&columns=isp&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=${
      this.props.widgetRecord.widget_id
    }&limit=1000&reportType=tree&include=ALL&reportDataType=0&tagsGrouping=custom-variable-1&valueFiltersGrouping=custom-variable-1&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc`;

    this.ISPURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_2bcf039b-b777-4d24-ad0d-2dd9fa978470/report/custom-variable-1,isp?dateRange=last-30-days&sortKey=profit&sortDirection=asc&page=1&chart=0&columns=customVariable1&columns=isp&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=${
      this.props.widgetRecord.widget_id
    }&limit=1000&reportType=tree&include=ALL&reportDataType=0&tagsGrouping=custom-variable-1&valueFiltersGrouping=custom-variable-1&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc`;

    this.monthsURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_32154ab0-b614-4ac5-b017-6d5a18447bc5/report/month?dateRange=last-30-days&sortKey=month&sortDirection=desc&page=1&chart=0&columns=month&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=100&reportType=&include=ACTIVE&reportDataType=0&tagsGrouping=month&valueFiltersGrouping=month&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc&filter2=custom-variable-1&filter2Value=${
      this.props.widgetRecord.widget_id
    }`;

    this.daysURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_32154ab0-b614-4ac5-b017-6d5a18447bc5/report/day?dateRange=last-30-days&sortKey=day&sortDirection=desc&page=1&chart=0&columns=day&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=100&reportType=&include=ACTIVE&reportDataType=0&tagsGrouping=day&valueFiltersGrouping=day&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc&filter2=custom-variable-1&filter2Value=${
      this.props.widgetRecord.widget_id
    }`;

    this.state = {
      clicked: false,
      hovered: false,
      domains: [],
      domainsClicked: false,
    };
  }

  componentDidMount() {
    if (
      this.props.widgetRecord.global_status === 'p_blacklist' ||
      this.props.widgetRecord.global_status === 'c_blacklist' ||
      this.props.widgetRecord.global_status === 'pc_blacklist'
    ) {
      this.setState({clicked: true});
    }
    let domains = this.props.widgetRecord.domain.split(',');
    this.setState({domains: domains});
  }

  colorizeRow(classification) {
    if (classification === 'white') {
      //green
      return '#eafcea';
    } else if (classification === 'black') {
      //red
      return '#f7d9d9';
    } else if (classification === 'grey') {
      //grey
      return '#ededed';
    } else if (classification === 'wait') {
      //light grey
      return '#fafafa';
    }
  }

  outlineRow(
    hovered,
    hasMismatchClassificationAndGlobalStatus,
    hasBadAndIncludedCampaigns,
  ) {
    if (
      hasMismatchClassificationAndGlobalStatus ||
      hasBadAndIncludedCampaigns
    ) {
      return 'red';
    } else if (hovered) {
      return 'black';
    } else {
      return 'transparent';
    }
  }

  showDomains() {
    if (this.state.domains.length === 1) {
      return (
        <a
          href={`https://refererhider.com/?http://${this.state.domains[0]}`}
          target={'_blank'}>
          {this.state.domains[0]}
        </a>
      );
    } else if (this.state.domainsClicked) {
      return (
        <div>
          <p
            onClick={e => {
              e.stopPropagation();
              this.setState({domainsClicked: false, clicked: false});
            }}>
            hide multiples &#8679;
          </p>
          {this.state.domains.map(domain => (
            <div key={domain}>
              <a
                href={`https://refererhider.com/?http://${domain}`}
                target={'_blank'}>
                {domain}
              </a>
            </div>
          ))}
        </div>
      );
    } else {
      return (
        <p
          onClick={e => {
            e.stopPropagation();
            this.setState({domainsClicked: true, clicked: false});
          }}>
          show multiples &#8681;
        </p>
      );
    }
  }

  render() {
    return (
      <tr
        style={{
          backgroundColor: this.colorizeRow(
            this.props.widgetRecord.classification,
          ),
          outlineStyle: 'solid',
          outlineColor: this.outlineRow(
            this.state.hovered,
            this.props.widgetRecord
              .has_mismatch_classification_and_global_status,
            this.props.widgetRecord.has_bad_and_included_campaigns,
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
          {this.props.widgetRecord.widget_id}
          <div>
            <InternalLink
              className={'rowLink'}
              stopPropagation={true}
              to={`/campaignsforonecwidget/${
                this.props.widgetRecord.widget_id
              }`}
              target={'_blank'}
              label={'campaigns'}
            />

            <InternalLink
              className={'rowLink'}
              stopPropagation={true}
              to={`/campaignsforonepwidget/${this.props.widgetRecord.widget_id.match(
                /^\d*/,
              )}`}
              target={'_blank'}
              label={'p_widgets'}
            />

            <InternalLink
              className={'rowLink'}
              stopPropagation={true}
              to={`/cwidgetsforonepwidget/${this.props.widgetRecord.widget_id.match(
                /^\d*/,
              )}`}
              target={'_blank'}
              label={'c_widgets'}
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
              href={this.deviceOSURL}
              target={'_blank'}
              label={'device/os'}
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
              to={`/monthsforonecwidgetforallcampaigns/${
                this.props.widgetRecord.widget_id
              }`}
              target={'_blank'}
              label={'months'}
            />

            <InternalLink
              className={'rowLink'}
              stopPropagation={true}
              to={`/daysforonecwidgetforallcampaigns/${
                this.props.widgetRecord.widget_id
              }`}
              target={'_blank'}
              label={'days'}
            />

            <InternalLink
              className={'rowLink'}
              to={`/excludecwidgetconfirmation/${
                this.props.widgetRecord.widget_id
              }`}
              target={'_blank'}
              label={'exclude'}
            />
          </div>
        </td>
        <td>
          {this.showDomains()}
          {this.props.widgetRecord.domain.length > 0 && (
            <div>
              <Link
                onClick={e => e.stopPropagation()}
                to={{
                  pathname: `/pwidgetsforonedomainforallcampaigns/${
                    this.props.widgetRecord.domain
                  }/`,
                }}
                target="_blank">
                widgets
              </Link>
            </div>
          )}
        </td>
        <td>
          {this.props.widgetRecord.classification !== 'wait' ? (
            <div>
              <Link
                onClick={e => e.stopPropagation()}
                to={{
                  pathname: `/listcwidgetconfirmation/${
                    this.props.widgetRecord.widget_id
                  }/${this.props.widgetRecord.classification}`,
                }}
                target="_blank">
                {this.props.widgetRecord.classification}
              </Link>
              <div>
                {`(${this.props.widgetRecord.good_campaigns_count}g/${
                  this.props.widgetRecord.bad_campaigns_count
                }b/${this.props.widgetRecord.wait_campaigns_count}w)`}
              </div>
            </div>
          ) : (
            <div>
              <div>wait</div>
              <div>
                {`(${this.props.widgetRecord.good_campaigns_count}g/${
                  this.props.widgetRecord.bad_campaigns_count
                }b/${this.props.widgetRecord.wait_campaigns_count}w)`}
              </div>
            </div>
          )}
        </td>
        <td>${this.props.widgetRecord.cost}</td>
        <td>${this.props.widgetRecord.revenue}</td>
        <td>${this.props.widgetRecord.profit}</td>
        <td>{this.props.widgetRecord.clicks}</td>
        <td>{this.props.widgetRecord.cpc}</td>
        <td>{this.props.widgetRecord.epc}</td>
        <td>{this.props.widgetRecord.leads}</td>
        <td>${this.props.widgetRecord.cpl}</td>
        <td>${this.props.widgetRecord.epl}</td>
        <td>{this.props.widgetRecord.lead_cvr}%</td>
        <td>{this.props.widgetRecord.sales}</td>
        <td>${this.props.widgetRecord.cps}</td>
        <td>${this.props.widgetRecord.eps}</td>
        <td>
          {this.props.widgetRecord.global_status}
          <div onClick={() => this.setState({clicked: true})}>
            <InternalLink
              className={'rowLink'}
              to={`/listcwidgetconfirmation/${
                this.props.widgetRecord.widget_id
              }/white`}
              target={'_blank'}
              label={'white'}
            />
            <InternalLink
              className={'rowLink'}
              to={`/listcwidgetconfirmation/${
                this.props.widgetRecord.widget_id
              }/grey`}
              target={'_blank'}
              label={'grey'}
            />
            <InternalLink
              className={'rowLink'}
              to={`/listcwidgetconfirmation/${
                this.props.widgetRecord.widget_id
              }/black`}
              target={'_blank'}
              label={'black'}
            />
          </div>
        </td>
      </tr>
    );
  }
}

export default Record;
