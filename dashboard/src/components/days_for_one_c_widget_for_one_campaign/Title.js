//@format
import React from 'react';
import {Helmet} from 'react-helmet';

const Title = props => {
  let title = `days for one c widget (${props.cWidgetID}) for one campaign (${
    props.name
  })`;
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
