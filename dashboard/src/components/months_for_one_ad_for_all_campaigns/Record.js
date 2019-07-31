//@format
import React, {Component} from 'react';
import convertMonthNumberToMonthWord from './convertMonthNumberToMonthWord';

class Record extends Component {
  constructor(props) {
    super(props);
    this.state = {clicked: false, hovered: false};
  }

  outlineRow(hovered) {
    if (hovered) {
      return 'black';
    } else {
      return 'transparent';
    }
  }

  render() {
    return (
      <tr
        style={{
          outlineStyle: 'solid',
          outlineColor: this.outlineRow(this.state.hovered),
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
        <td>{convertMonthNumberToMonthWord(this.props.monthRecord.month)}</td>
        <td>${this.props.monthRecord.cost}</td>
        <td>${this.props.monthRecord.revenue}</td>
        <td>${this.props.monthRecord.profit}</td>
        <td>{this.props.monthRecord.clicks}</td>
        <td>${this.props.monthRecord.cpc}</td>
        <td>${this.props.monthRecord.epc}</td>
        <td>{this.props.monthRecord.leads}</td>
        <td>${this.props.monthRecord.cpl}</td>
        <td>${this.props.monthRecord.epl}</td>
        <td>{this.props.monthRecord.lead_cvr}%</td>
        <td>{this.props.monthRecord.sales}</td>
        <td>${this.props.monthRecord.cps}</td>
        <td>${this.props.monthRecord.eps}</td>
        <td>{this.props.monthRecord.roi}%</td>
      </tr>
    );
  }
}

export default Record;
