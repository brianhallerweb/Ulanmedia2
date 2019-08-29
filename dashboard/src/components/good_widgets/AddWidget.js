import React, { Component } from "react";

class AddWidget extends Component {
  constructor(props) {
    super(props);
    this.state = {
    };
  }

  handleAdd(e) {
    e.preventDefault();
    const widget = e.target.elements.newWidget.value.trim();
    this.props.handleAdd(widget);
    e.target.elements.newWidget.value = "";
  }

  render() {
    return (
      <div>
        {this.state.error && (
          <p className="add-widget-error">{this.state.error}</p>
        )}
        <form className="add-widget" onSubmit={this.handleAdd.bind(this)}>
          <input className="add-widget__input" type="text" name="newWidget" placeholder="5753946,5763297"/>
          <button className="button">Add widgets</button>
        </form>
      </div>
    );
  }
}

export default AddWidget;
