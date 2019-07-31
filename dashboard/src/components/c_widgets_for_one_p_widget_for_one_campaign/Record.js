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
      this.props.widgetRecord.status === 'excluded' ||
      this.props.widgetRecord.status === 'inactive'
    ) {
      this.setState({clicked: true});
    }
    let domains = this.props.widgetRecord.domain.split(',');
    this.setState({domains: domains});
  }

  addRowLinks() {
    const deviceOSURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_5a5a89b9-b146-4fb6-9ea4-128f8e675251/report/custom-variable-1,device,os?dateRange=last-30-days&sortKey=profit&sortDirection=asc&page=1&chart=0&columns=customVariable1&columns=isp&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=${
      this.props.widgetRecord.widget_id
    }&limit=1000&reportType=tree&include=ALL&reportDataType=0&tagsGrouping=custom-variable-1&valueFiltersGrouping=custom-variable-1&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc`;

    const ISPURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_2bcf039b-b777-4d24-ad0d-2dd9fa978470/report/custom-variable-1,isp?dateRange=last-30-days&sortKey=profit&sortDirection=asc&page=1&chart=0&columns=customVariable1&columns=isp&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=${
      this.props.widgetRecord.widget_id
    }&limit=1000&reportType=tree&include=ALL&reportDataType=0&tagsGrouping=custom-variable-1&valueFiltersGrouping=custom-variable-1&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc`;

    return (
      <div>
        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/campaignsforonecwidget/${this.props.widgetRecord.widget_id}`}
          target={'_blank'}
          label={'campaigns'}
        />
        <ExternalLink
          className={'rowLink'}
          href={`https://dashboard.mgid.com/advertisers/campaign-quality-analysis/id/${
            this.props.widgetRecord.mgid_id
          }?search=${this.props.widgetRecord.widget_id}`}
          target={'_blank'}
          label={'mgid'}
        />
        <ExternalLink
          className={'rowLink'}
          href={deviceOSURL}
          target={'_blank'}
          label={'device/os'}
        />
        <ExternalLink
          className={'rowLink'}
          href={ISPURL}
          target={'_blank'}
          label={'isp'}
        />
        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/monthsforonecwidgetforonecampaign/${
            this.props.widgetRecord.widget_id
          }/${this.props.widgetRecord.vol_id}/${
            this.props.widgetRecord.mgid_id
          }/${this.props.name}/`}
          target={'_blank'}
          label={'months'}
        />
        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/daysforonecwidgetforonecampaign/${
            this.props.widgetRecord.widget_id
          }/${this.props.widgetRecord.vol_id}/${
            this.props.widgetRecord.mgid_id
          }/${this.props.name}/`}
          target={'_blank'}
          label={'days'}
        />
        <InternalLink
          className={'rowLink'}
          to={`/excludecampaignforonecwidgetconfirmation/${
            this.props.widgetRecord.widget_id
          }/${this.props.widgetRecord.mgid_id}`}
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
            this.props.widgetRecord.is_bad_and_included,
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
          {this.props.widgetRecord.widget_id !== 'summary' &&
            this.addRowLinks()}
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
        {this.stylizeClassificationText(this.props.widgetRecord.classification)}
        <td>${this.props.widgetRecord.w_bid}</td>
        <td>${this.props.widgetRecord.rec_w_bid}</td>
        <td>{this.props.widgetRecord.coeff}</td>
        <td>{this.props.widgetRecord.rec_coeff}</td>
        <td>${this.props.widgetRecord.cost}</td>
        <td>${this.props.widgetRecord.revenue}</td>
        <td>${this.props.widgetRecord.profit}</td>
        <td>{this.props.widgetRecord.clicks}</td>
        <td>${this.props.widgetRecord.cpc}</td>
        <td>${this.props.widgetRecord.epc}</td>
        <td>{this.props.widgetRecord.leads}</td>
        <td>${this.props.widgetRecord.cpl}</td>
        <td>${this.props.widgetRecord.epl}</td>
        <td>${this.props.widgetRecord.mpl}</td>
        <td>{this.props.widgetRecord.sales}</td>
        <td>${this.props.widgetRecord.cps}</td>
        <td>${this.props.widgetRecord.eps}</td>
        <td>${this.props.widgetRecord.mps}</td>
        <td>{this.props.widgetRecord.status}</td>
        <td>{this.props.widgetRecord.global_status}</td>
      </tr>
    );
  }
}

export default Record;
