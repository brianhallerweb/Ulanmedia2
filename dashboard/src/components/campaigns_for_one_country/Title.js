//@format
import React from 'react';
import {Helmet} from 'react-helmet';

const Title = ({volRequestDates, countryName}) => {
  const title = `campaigns for one country (${countryName})`;
  return (
    <div className="title">
      <Helmet>
        <meta charSet="utf-8" />
        <title>{title}</title>
      </Helmet>

      <div className="title">
        <h3>{title}</h3>
        {volRequestDates && <p>(vol: {volRequestDates})</p>}
      </div>
    </div>
  );
};

export default Title;
