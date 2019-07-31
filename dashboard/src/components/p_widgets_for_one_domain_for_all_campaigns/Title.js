//@format
import React from 'react';
import {Helmet} from 'react-helmet';

const Title = ({domain}) => {
  const title = `p widgets for one domain for all campaigns (${domain})`;
  return (
    <div className="title">
      <Helmet>
        <meta charSet="utf-8" />
        <title>{title}</title>
      </Helmet>
      <h3>{title}</h3>
    </div>
  );
};

export default Title;
