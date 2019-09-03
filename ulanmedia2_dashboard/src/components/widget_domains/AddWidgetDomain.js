//@format
import React, {Component} from 'react';

class AddWidgetDomain extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  handleAdd(e) {
    e.preventDefault();
    const widgetDomains = e.target.elements.newWidgetDomains.value.trim();
    this.props.handleAdd(widgetDomains);
    e.target.elements.newWidgetDomains.value = '';
  }

  render() {
    return (
      <div>
        {this.state.error && <p>{this.state.error}</p>}
        <form onSubmit={this.handleAdd.bind(this)}>
          <textarea
            name="newWidgetDomains"
            placeholder="traffic source 1, widget id 1, domain 1, widget_domain_source 1                                                                      traffic source 2, widget id 2, domain 2, widget_domain source 2"
            rows={15}
            cols={50}
          />
          <button className="button">Add widget domains</button>
        </form>
      </div>
    );
  }
}

export default AddWidgetDomain;
