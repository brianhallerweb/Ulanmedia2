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
            <th>Image</th>
            <th>Global Rank</th>
            <th>Classification</th>
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
          {this.props.adsRecords.map(adRecord => (
            <Record key={adRecord.image} ad={adRecord} />
          ))}
        </tbody>
      </table>
    );
  }

  render() {
    return (
      <div>
        {this.props.loading && <div className="loader" />}
        {this.props.error && !this.props.loading && <p>no ads found</p>}
        {this.props.adsRecords.length > 0 &&
          !this.props.loading &&
          this.createTable()}
      </div>
    );
  }
}

export default Records;
