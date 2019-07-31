//@format
import React from 'react';
import {Helmet} from 'react-helmet';

const Title = props => {
  let title = '';
  if (props.dayRecords.length > 0) {
    title = `days for one campaign (${props.dayRecords[0].name})`;
  }
  return (
    <div>
      {props.dayRecords.length > 0 && (
        <div>
          <Helmet>
            <meta charSet="utf-8" />
            <title>{title}</title>
          </Helmet>
          <h3>{title}</h3>
        </div>
      )}
    </div>
  );
};

export default Title;
