//@format
import React from 'react';
import {Helmet} from 'react-helmet';

const Title = () => {
  const title = `Widget Domains`;
  return (
    <div style={{marginTop: 30, marginBottom: 40}}>
      <Helmet>
        <meta charSet="utf-8" />
        <title>{title}</title>
      </Helmet>
      <h3>{title}</h3>
    </div>
  );
};

export default Title;
