//@format
import React from 'react';
import Widget from './Widget';

const Widgets = ({widgets, handleDelete}) => {
  return (
    <div>
      <div>
        {widgets.map(widget => (
          <Widget
            key={widget.widget_id}
            widgetID={widget.widget_id}
            handleDelete={handleDelete}
          />
        ))}
      </div>
    </div>
  );
};

export default Widgets;
