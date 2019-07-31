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
            <th>Offer Name</th>
            <th>Classification</th>
            <th>Score (roi+cvr+gpr)</th>
            <th>Vol Weight</th>
            <th>Rec Weight</th>
            <th>Cost*</th>
            <th>Revenue</th>
            <th>Profit*</th>
            <th>Clicks*</th>
            <th>CPC*</th>
            <th>EPC</th>
            <th>Leads</th>
            <th>CPL*</th>
            <th>EPL</th>
            <th>Lead CVR*</th>
            <th>Sales</th>
            <th>CPS*</th>
            <th>EPS</th>
            <th>ROI*</th>
          </tr>
        </thead>
        <tbody>
          {this.props.offersRecords.map(offerRecord => (
            <Record
              key={offerRecord.offer_id}
              offer={offerRecord}
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
        {this.props.error && !this.props.loading && <p>no offers found</p>}
        {this.props.offersRecords.length > 0 &&
          !this.props.loading &&
          this.createTable()}
      </div>
    );
  }
}

export default Records;
