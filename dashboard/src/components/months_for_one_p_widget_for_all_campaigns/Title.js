//@format
import React from 'react';
import {Helmet} from 'react-helmet';

const Title = props => {
  let title = `months for one p widget for all campaigns (${props.pWidgetID})`;
  return (
    <div>
      <Helmet>
        <meta charSet="utf-8" />
        <title>{title}</title>
      </Helmet>
      <div className="title">
        <h3>{title}</h3>
        {props.volRequestDates && <p>(vol: {props.volRequestDates})</p>}
      </div>
    </div>
  );
};

export default Title;
