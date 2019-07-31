//@format
import React from 'react';
import {Helmet} from 'react-helmet';

const Title = ({volRequestDates}) => {
  const title = 'countries for all campaigns';
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
