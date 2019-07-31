//@format
import React from 'react';
import {Helmet} from 'react-helmet';

const Title = ({ID, mgidRequestDates, volRequestDates}) => {
  const title = `campaigns for one p widget (${ID})`;
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
