//@format
import React from 'react';

const WidgetDomain = ({trafficSource, widgetID, domain, handleDelete}) => {
  return (
    <tr key={widgetID}>
      <td>{trafficSource}</td>
      <td>{widgetID}</td>
      <td>{domain}</td>
      <td>
        <button onClick={() => handleDelete(trafficSource, widgetID, domain)}>Remove</button>
      </td>
    </tr>
  );
};

export default WidgetDomain;
