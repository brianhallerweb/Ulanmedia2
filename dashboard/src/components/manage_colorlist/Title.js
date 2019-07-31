//@format
import React from 'react';
import {Helmet} from 'react-helmet';

const Title = ({color}) => {
  const title = `Complete ${color}list`;
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
