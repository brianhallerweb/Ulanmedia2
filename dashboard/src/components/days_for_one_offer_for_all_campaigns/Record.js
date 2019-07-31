//@format
import React, {Component} from 'react';

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
        <td>{this.props.dayRecord.day}</td>
        <td>${this.props.dayRecord.cost}</td>
        <td>${this.props.dayRecord.revenue}</td>
        <td>${this.props.dayRecord.profit}</td>
        <td>{this.props.dayRecord.clicks}</td>
        <td>${this.props.dayRecord.cpc}</td>
        <td>${this.props.dayRecord.epc}</td>
        <td>{this.props.dayRecord.leads}</td>
        <td>${this.props.dayRecord.cpl}</td>
        <td>${this.props.dayRecord.epl}</td>
        <td>{this.props.dayRecord.lead_cvr}%</td>
        <td>{this.props.dayRecord.sales}</td>
        <td>${this.props.dayRecord.cps}</td>
        <td>${this.props.dayRecord.eps}</td>
        <td>{this.props.dayRecord.roi}%</td>
      </tr>
    );
  }
}

export default Record;
