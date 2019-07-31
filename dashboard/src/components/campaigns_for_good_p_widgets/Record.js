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
        <ExternalLink
          className={'rowLink'}
          href={`https://dashboard.mgid.com/advertisers/campaign-quality-analysis/id/${
            this.props.campaignRecord.mgid_id
          }?search=${this.props.campaignRecord.widget_id.match(/^\d*/)}`}
          target={'_blank'}
          label={'mgid'}
        />

        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/monthsforonepwidgetforonecampaign/${this.props.campaignRecord.widget_id.match(
            /^\d*/,
          )}/${this.props.campaignRecord.vol_id}/${
            this.props.campaignRecord.name
          }/`}
          target={'_blank'}
          label={'months'}
        />

        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/daysforonepwidgetforonecampaign/${this.props.campaignRecord.widget_id.match(
            /^\d*/,
          )}/${this.props.campaignRecord.vol_id}/${
            this.props.campaignRecord.name
          }/`}
          target={'_blank'}
          label={'days'}
        />
      </div>
    );
  }

  outlineRow(hovered, mismatchWBidAndRecWBid, mismatchCoeffAndRecCoeff) {
    if (mismatchWBidAndRecWBid || mismatchCoeffAndRecCoeff) {
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
          outlineStyle: 'solid',
          outlineColor: this.outlineRow(
            this.state.hovered,
            this.props.campaignRecord.mismatch_w_bid_and_rec_w_bid,
            this.props.campaignRecord.mismatch_coeff_and_rec_coeff,
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
        <td>{this.props.campaignRecord.widget_id}</td>
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
        <td>{this.props.campaignRecord.global_status}</td>
      </tr>
    );
  }
}

export default Record;
