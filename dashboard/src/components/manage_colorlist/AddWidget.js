import React, { Component } from "react";

class AddWidget extends Component {
  constructor(props) {
    super(props);
    this.state = {
      error: undefined
    };
  }

  handleAdd(e) {
    e.preventDefault();
    const widget = e.target.elements.newWidget.value.trim();
    const error = this.props.handleAdd(widget);
    this.setState(() => ({ error }));

    if (!this.error) {
      e.target.elements.newWidget.value = "";
    }
  }

  render() {
    return (
      <div>
        {this.state.error && (
          <p className="add-widget-error">{this.state.error}</p>
        )}
        <form className="add-widget" onSubmit={this.handleAdd.bind(this)}>
          <input className="add-widget__input" type="text" name="newWidget" />
          <button className="button">Add new widget</button>
        </form>
      </div>
    );
  }
}

export default AddWidget;
