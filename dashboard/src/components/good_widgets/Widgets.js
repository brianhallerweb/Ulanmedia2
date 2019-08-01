//@format
import React from 'react';
import Widget from './Widget';

const Widgets = ({widgets, handleDelete}) => {
  return (
    <table style={{marginTop: 30, width: '50%'}}>
      <thead>
        <tr>
          <th>Widget ID</th>
          <th />
        </tr>
      </thead>
      <tbody>
        {widgets.map(widget => (
          <Widget
            key={widget.widget_id}
            widgetID={widget.widget_id}
            handleDelete={handleDelete}
          />
        ))}
      </tbody>
    </table>
  );
};

export default Widgets;
