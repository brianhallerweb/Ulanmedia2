//@format
import React from 'react';
import {Helmet} from 'react-helmet';

const Title = ({name, mgidRequestDates, volRequestDates}) => {
  const title = `p widgets for one campaign (${name})`;
  return (
    <div className="title">
      <Helmet>
        <meta charSet="utf-8" />
        <title>{title}</title>
      </Helmet>
      <h3>{title}</h3>
      {volRequestDates && <p>(vol: {volRequestDates})</p>}
      {mgidRequestDates && <p>(mgid: {mgidRequestDates})</p>}
    </div>
  );
};

export default Title;
