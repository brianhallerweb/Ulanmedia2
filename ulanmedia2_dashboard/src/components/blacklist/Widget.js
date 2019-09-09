//@format
import React from 'react';

const Widget = ({widgetID, handleDelete}) => {
  return (
    <tr key={widgetID}>
      <td>{widgetID}</td>
      <td>
        <button onClick={() => handleDelete(widgetID)}>Remove</button>
      </td>
    </tr>
  );
};

export default Widget;
