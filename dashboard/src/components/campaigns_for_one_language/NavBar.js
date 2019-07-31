//@format
import React, {Component} from 'react';
import DatesDropdown from './DatesDropdown';
import ConditionCheckboxes from './ConditionCheckboxes';

class NavBar extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div>
        <form
          onSubmit={e => {
            e.preventDefault();
            this.props.submitForm();
          }}>
          <DatesDropdown
            selectDateRange={this.props.selectDateRange}
            dateRange={this.props.dateRange}
          />
          <ConditionCheckboxes
            toggleCondition={this.props.toggleCondition}
            setConditionValue={this.props.setConditionValue}
            loading={this.props.loading}
            c1={this.props.c1}
            c1Value={this.props.c1Value}
            c2={this.props.c2}
            c2Value={this.props.c2Value}
          />
          <div style={{marginBottom: 10}}>
            *Remember the Cost, Profit, Clicks, CPC, CPL, Lead CVR, CPS, and ROI
            are not highly accurate, they're just estimates based on Voluum's
            daily averaged CPC evenly distributed across received
            clicks....instead of being based on MGID's variable CPC actual
            charged clicks.
          </div>

          <input type="submit" value="Submit" disabled={this.props.loading} />
        </form>
      </div>
    );
  }
}

export default NavBar;
