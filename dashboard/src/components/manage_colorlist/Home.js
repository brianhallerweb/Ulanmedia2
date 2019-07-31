//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import Title from './Title';
import Widgets from './Widgets';
import AddWidget from './AddWidget';
import {Redirect} from 'react-router-dom';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      color: this.props.match.params.color,
      widgets: [],
      authenticated: true,
    };
  }

  componentDidMount() {
    fetch(`/jsonapi/completecolorlist/${this.state.color}`)
      .then(res => res.json())
      .then(list => {
        this.setState({widgets: list[`${this.state.color}list`]});
      });
  }

  handleAdd(widget) {
    if (!widget) return 'Enter a valid widget';

    const widgets = widget.split(',');
    for (let widget of widgets) {
      widget = widget.trim();
      if (widget) {
        fetch(`/jsonapi/colorlist/${this.state.color}`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            widget_id: widget,
          }),
        })
          .then(() => fetch(`/jsonapi/completecolorlist/${this.state.color}`))
          .then(res => res.json())
          .then(list => {
            this.setState({widgets: list[`${this.state.color}list`]});
          });
      }
    }
  }

  handleDelete(widget) {
    fetch(`/jsonapi/colorlist/${this.state.color}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        widget_id: widget,
      }),
    })
      .then(() => fetch(`/jsonapi/completecolorlist/${this.state.color}`))
      .then(res => res.json())
      .then(list => {
        this.setState({widgets: list[`${this.state.color}list`]});
      });
  }

  render() {
    return (
      <div>
        <Title color={this.state.color} />
        <AddWidget handleAdd={this.handleAdd.bind(this)} />
        <Widgets
          widgets={this.state.widgets}
          handleDelete={this.handleDelete.bind(this)}
        />
      </div>
    );
  }
}

export default Home;
