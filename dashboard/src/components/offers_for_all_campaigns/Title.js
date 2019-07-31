//@format
import React from 'react';
import {Helmet} from 'react-helmet';

const Title = ({volRequestDates}) => {
  const title = `offers for all campaigns`;
  return (
    <div className="title">
      <Helmet>
        <meta charSet="utf-8" />
        <title>{title}</title>
      </Helmet>
      <h3>{title}</h3>
      {volRequestDates && <p>(vol: {volRequestDates})</p>}
    </div>
  );
};

export default Title;
