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
            <th>Classification</th>
            <th>Cost</th>
            <th>Revenue</th>
            <th>Profit</th>
            <th>Clicks</th>
            <th>CPC</th>
            <th>EPC</th>
            <th>MPC</th>
            <th>Leads</th>
            <th>CPL</th>
            <th>EPL</th>
            <th>MPL</th>
            <th>Sales</th>
            <th>CPS</th>
            <th>EPS</th>
            <th>MPS</th>
          </tr>
        </thead>
        <tbody>
          {this.props.campaignsRecords.map(campaignRecord => (
            <Record
              key={campaignRecord.name}
              campaign={campaignRecord}
              volRequestStartDate={this.props.volRequestStartDate}
              volRequestEndDate={this.props.volRequestEndDate}
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
        {this.props.campaignsRecords.length > 0 &&
          !this.props.loading &&
          this.createTable()}
      </div>
    );
  }
}

export default Records;
