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
            <th>Cost*</th>
            <th>Revenue</th>
            <th>Profit*</th>
            <th>Clicks*</th>
            <th>CPC*</th>
            <th>EPC</th>
            <th>Conversions</th>
            <th>CPA*</th>
            <th>EPA</th>
            <th>CVR*</th>
            <th>ROI*</th>
          </tr>
        </thead>
        <tbody>
          {this.props.languagesRecords.map(languagesRecord => (
            <Record
              key={languagesRecord.campaign_id}
              language={languagesRecord}
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
        {this.props.languagesRecords.length > 0 &&
          !this.props.loading &&
          this.createTable()}
      </div>
    );
  }
}

export default Records;
