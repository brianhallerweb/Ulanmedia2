//@format
import React from 'react';

const Widget = ({widgetID, handleDelete}) => {
  return (
    <div>
      <p>
        {widgetID + ' '}
        <button onClick={() => handleDelete(widgetID)}>X</button>
      </p>
    </div>
  );
};

export default Widget;
