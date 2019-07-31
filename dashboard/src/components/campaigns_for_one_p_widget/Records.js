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
            <th>Domain</th>
            <th>Classification</th>
            <th>W Bid</th>
            <th>Rec W Bid</th>
            <th>Coeff</th>
            <th>Rec Coeff</th>
            <th>Cost</th>
            <th>Revenue</th>
            <th>Profit</th>
            <th>Clicks</th>
            <th>CPC</th>
            <th>EPC</th>
            <th>Leads</th>
            <th>CPL</th>
            <th>EPL</th>
            <th>MPL</th>
            <th>Sales</th>
            <th>CPS</th>
            <th>EPS</th>
            <th>MPS</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {this.props.campaignRecords.map(campaignRecord => (
            <Record
              key={campaignRecord.mgid_id}
              campaignRecord={campaignRecord}
              pWidgetHasChildren={this.props.pWidgetHasChildren}
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
        {this.props.campaignRecords.length > 0 &&
          !this.props.loading &&
          this.createTable()}
      </div>
    );
  }
}

export default Records;
