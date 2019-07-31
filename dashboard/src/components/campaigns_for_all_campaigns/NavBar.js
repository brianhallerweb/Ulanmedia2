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
            c2={this.props.c2}
            c3={this.props.c3}
            c4={this.props.c4}
            c5={this.props.c5}
            c6={this.props.c6}
            c7={this.props.c7}
            c8={this.props.c8}
            c9={this.props.c9}
            c10={this.props.c10}
            c11={this.props.c11}
            c12={this.props.c12}
            c13={this.props.c13}
            c14={this.props.c14}
            c15={this.props.c15}
            c16={this.props.c16}
            c17={this.props.c17}
            c18={this.props.c18}
            c19={this.props.c19}
            c20={this.props.c20}
            c21={this.props.c21}
            c22={this.props.c22}
            c23={this.props.c23}
            c24={this.props.c24}
            c25={this.props.c25}
            c26={this.props.c26}
            c27={this.props.c27}
            c1Value={this.props.c1Value}
            c2Value={this.props.c2Value}
            c3Value={this.props.c3Value}
            c6Value={this.props.c6Value}
            c7Value={this.props.c7Value}
            c8Value={this.props.c8Value}
            c9Value={this.props.c9Value}
            c10Value={this.props.c10Value}
            c11Value={this.props.c11Value}
            c12Value={this.props.c12Value}
            c13Value={this.props.c13Value}
            c14Value={this.props.c14Value}
            c15Value={this.props.c15Value}
            c16Value={this.props.c16Value}
            c17Value={this.props.c17Value}
            c18Value={this.props.c18Value}
            c19Value={this.props.c19Value}
            c20Value={this.props.c20Value}
            c21Value={this.props.c21Value}
            c22Value={this.props.c22Value}
            c23Value={this.props.c23Value}
            c24Value={this.props.c24Value}
            c25Value={this.props.c25Value}
            c26Value={this.props.c26Value}
            c27Value={this.props.c27Value}
          />
          <input type="submit" value="Submit" disabled={this.props.loading} />
        </form>
      </div>
    );
  }
}

export default NavBar;
