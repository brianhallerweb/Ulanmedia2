//@format
import React from 'react';

const Widget = ({widgetID, domain, handleDelete}) => {
  return (
    <tr key={widgetID}>
      <td>{widgetID}</td>
      <td>{domain}</td>
      <td>
        <button onClick={() => handleDelete(widgetID)}>Remove</button>
      </td>
    </tr>
  );
};

export default Widget;
