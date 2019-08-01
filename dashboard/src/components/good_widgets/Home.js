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
      widgets: [],
      authenticated: true,
    };
  }

  componentDidMount() {
    fetch(`/jsonapi/completegoodwidgets`)
      .then(res => res.json())
      .then(widgets => {
        this.setState({widgets: widgets['good list']});
      });
  }

  handleAdd(widget) {
    if (!widget) return 'Enter a valid widget';

    const widgets = widget.split(',');
    for (let widget of widgets) {
      widget = widget.trim();
      if (widget) {
        fetch(`/jsonapi/goodwidget`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            widget_id: widget,
          }),
        })
          .then(() => fetch(`/jsonapi/completegoodwidgets`))
          .then(res => res.json())
          .then(widgets => {
            this.setState({widgets: widgets['good list']});
          });
      }
    }
  }

  handleDelete(widget) {
    fetch(`/jsonapi/goodwidget`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        widget_id: widget,
      }),
    })
      .then(() => fetch(`/jsonapi/completegoodwidgets`))
      .then(res => res.json())
      .then(widgets => {
        this.setState({widgets: widgets['good list']});
      });
  }

  render() {
    return (
      <div>
        <Title />
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
