//@format
import React from 'react';
import WidgetDomain from './WidgetDomain';

const WidgetDomains = ({widgetDomains, handleDelete}) => {
  return (
    <table style={{marginTop: 30, width: '50%'}}>
      <thead>
        <tr>
          <th>Traffic Source</th>
          <th>Widget ID</th>
          <th>Domain</th>
          <th />
        </tr>
      </thead>
      <tbody>
        {widgetDomains.map(widgetDomain => (
          <WidgetDomain
            key={widgetDomain.id}
            trafficSource={widgetDomain.traffic_source}
            widgetID={widgetDomain.widget_id}
            domain={widgetDomain.domain}
            handleDelete={handleDelete}
          />
        ))}
      </tbody>
    </table>
  );
};

export default WidgetDomains;
