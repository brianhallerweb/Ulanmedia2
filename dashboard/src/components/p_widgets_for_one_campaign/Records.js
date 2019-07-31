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
            <th>P Widget</th>
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
            <th>Global Status</th>
          </tr>
        </thead>
        <tbody>
          {this.props.widgetRecords.map(widgetRecord => (
            <Record
              key={widgetRecord.widget_id}
              widgetRecord={widgetRecord}
              name={this.props.name}
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
        {this.props.error && !this.props.loading && <p>no p widgets found</p>}
        {this.props.widgetRecords.length > 0 &&
          !this.props.loading &&
          this.createTable()}
      </div>
    );
  }
}

export default Records;
