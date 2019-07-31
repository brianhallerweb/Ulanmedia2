//@format
import React, {Component} from 'react';
import Record from './Record';

class Records extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  createTable() {
    return (
      <table>
        <thead>
          <tr>
            <th>Campaign</th>
            <th>Cost</th>
            <th>Revenue</th>
            <th>Profit</th>
            <th>Impressions</th>
            <th>PPI</th>
            <th>Clicks</th>
            <th>CTR</th>
            <th>CPC</th>
            <th>EPC</th>
            <th>Leads</th>
            <th>CPL</th>
            <th>EPL</th>
            <th>Lead CVR</th>
            <th>Sales</th>
            <th>CPS</th>
            <th>EPS</th>
            <th>ROI</th>
          </tr>
        </thead>
        <tbody>
          {this.props.campaignRecords.map(campaignRecord => (
            <Record
              key={campaignRecord.mgid_id}
              campaign={campaignRecord}
              adImage={this.props.adImage}
            />
          ))}
        </tbody>
      </table>
    );
  }

  render() {
    return (
      <div>
        {this.props.loading && <div className="loader" />}
        {this.props.error && !this.props.loading && <p>no campaigns found</p>}
        {this.props.campaignRecords.length > 0 &&
          !this.props.loading &&
          this.createTable()}
      </div>
    );
  }
}

export default Records;
