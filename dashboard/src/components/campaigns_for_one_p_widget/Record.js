//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import InternalLink from '../utilities/InternalLink';
import ExternalLink from '../utilities/ExternalLink';

class Record extends Component {
  constructor(props) {
    super(props);
    this.state = {
      clicked: false,
      hovered: false,
      domains: [],
      domainsClicked: false,
    };
  }

  componentDidMount() {
    if (
      this.props.campaignRecord.status === 'excluded' ||
      this.props.campaignRecord.status === 'inactive'
    ) {
      this.setState({clicked: true});
    }
    let domains = this.props.campaignRecord.domain.split(',');
    this.setState({domains: domains});
  }

  addRowLinks() {
    return (
      <div>
        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/pwidgetsforonecampaign/${this.props.campaignRecord.vol_id}/${
            this.props.campaignRecord.name
          }/
              `}
          target={'_blank'}
          label={'p_widgets'}
        />

        {this.props.pWidgetHasChildren && (
          <InternalLink
            className={'rowLink'}
            stopPropagation={true}
            to={`/cwidgetsforonepwidgetforonecampaign/${
              this.props.campaignRecord.vol_id
            }/${this.props.campaignRecord.widget_id.match(/^\d*/)}/${
              this.props.campaignRecord.name
            }/`}
            target={'_blank'}
            label={'c_widgets'}
          />
        )}

        <ExternalLink
          className={'rowLink'}
          stopPropagation={true}
          href={`https://dashboard.mgid.com/advertisers/campaign-quality-analysis/id/${
            this.props.campaignRecord.mgid_id
          }?search=${this.props.campaignRecord.widget_id.match(/^\d*/)}`}
          target={'_blank'}
          label={'mgid'}
        />

        <ExternalLink
          className={'rowLink'}
          href={`https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_bb64816c-68a9-4d9d-9612-3ef60a6f4a0a/report/custom-variable-1,country-code?dateRange=custom-date&sortKey=cost&sortDirection=desc&page=1&chart=0&columns=customVariable1&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=${
            this.props.campaignRecord.widget_id
          }&limit=100&reportType=&include=ALL&reportDataType=0&tagsGrouping=custom-variable-1&valueFiltersGrouping=custom-variable-1&from=${
            this.props.volRequestStartDate
          }T00:00:00Z&to=${
            this.props.volRequestEndDate
          }T00:00:00Z&filter1=campaign&filter1Value=${
            this.props.campaignRecord.vol_id
          }`}
          target={'_blank'}
          label={'countries'}
        />

        <ExternalLink
          className={'rowLink'}
          href={`https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_b6af5a4f-6dc5-4bdb-b749-bf2eba7cb3fc/report/custom-variable-1,language?dateRange=custom-date&sortKey=visits&sortDirection=desc&page=1&chart=0&columns=customVariable1&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=${
            this.props.campaignRecord.widget_id
          }&limit=100&reportType=&include=ALL&reportDataType=0&tagsGrouping=custom-variable-1&valueFiltersGrouping=custom-variable-1&from=${
            this.props.volRequestStartDate
          }T00:00:00Z&to=${
            this.props.volRequestEndDate
          }T00:00:00Z&filter1=campaign&filter1Value=${
            this.props.campaignRecord.vol_id
          }`}
          target={'_blank'}
          label={'languages'}
        />

        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/monthsforonepwidgetforonecampaign/${this.props.campaignRecord.widget_id.match(
            /^\d*/,
          )}/${this.props.campaignRecord.vol_id}/${
            this.props.campaignRecord.mgid_id
          }/${this.props.campaignRecord.name}/`}
          target={'_blank'}
          label={'months'}
        />

        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/daysforonepwidgetforonecampaign/${this.props.campaignRecord.widget_id.match(
            /^\d*/,
          )}/${this.props.campaignRecord.vol_id}/${
            this.props.campaignRecord.mgid_id
          }/${this.props.campaignRecord.name}/`}
          target={'_blank'}
          label={'days'}
        />

        <InternalLink
          className={'rowLink'}
          to={`/excludecampaignforonepwidgetconfirmation/${this.props.campaignRecord.widget_id.match(
            /^\d*/,
          )}/${this.props.campaignRecord.mgid_id}`}
          target={'_blank'}
          label={'exclude'}
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
    } else if (classification === 'wait') {
      //light grey
      return '#fafafa';
    }
  }

  outlineRow(hovered, isBadAndIncluded) {
    if (isBadAndIncluded) {
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
          onClick={e => {
            e.stopPropagation();
          }}
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
                onClick={e => {
                  e.stopPropagation();
                }}
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
            this.props.campaignRecord.classification,
          ),
          outlineStyle: 'solid',
          outlineColor: this.outlineRow(
            this.state.hovered,
            this.props.campaignRecord.is_bad_and_included,
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
          {this.props.campaignRecord.name}
          {this.props.campaignRecord.name !== 'summary' && this.addRowLinks()}
        </td>
        <td>
          {this.showDomains()}
          {this.props.campaignRecord.domain.length > 0 && (
            <div>
              <Link
                onClick={e => e.stopPropagation()}
                to={{
                  pathname: `/pwidgetsforonedomainforallcampaigns/${
                    this.props.campaignRecord.domain
                  }/`,
                }}
                target="_blank">
                widgets
              </Link>
            </div>
          )}
        </td>
        {this.stylizeClassificationText(
          this.props.campaignRecord.classification,
        )}
        <td>${this.props.campaignRecord.w_bid}</td>
        <td>${this.props.campaignRecord.rec_w_bid}</td>
        <td>{this.props.campaignRecord.coeff}</td>
        <td>{this.props.campaignRecord.rec_coeff}</td>
        <td>${this.props.campaignRecord.cost}</td>
        <td>${this.props.campaignRecord.revenue}</td>
        <td>${this.props.campaignRecord.profit}</td>
        <td>{this.props.campaignRecord.clicks}</td>
        <td>${this.props.campaignRecord.cpc}</td>
        <td>${this.props.campaignRecord.epc}</td>
        <td>{this.props.campaignRecord.leads}</td>
        <td>${this.props.campaignRecord.cpl}</td>
        <td>${this.props.campaignRecord.epl}</td>
        <td>${this.props.campaignRecord.mpl}</td>
        <td>{this.props.campaignRecord.sales}</td>
        <td>${this.props.campaignRecord.cps}</td>
        <td>${this.props.campaignRecord.eps}</td>
        <td>${this.props.campaignRecord.mps}</td>
        <td>{this.props.campaignRecord.status}</td>
      </tr>
    );
  }
}

export default Record;
