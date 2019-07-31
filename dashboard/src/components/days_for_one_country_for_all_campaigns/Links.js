//@format
import React from 'react';
import InternalLink from '../utilities/InternalLink';

const Links = props => {
  return (
    <div>
      <InternalLink
        className={'rowLink'}
        stopPropagation={true}
        to={`/monthsforonecountryforallcampaigns/${props.countryName}`}
        target={'_blank'}
        label={'Months'}
      />
      <InternalLink
        className={'rowLink'}
        stopPropagation={true}
        to={`/daysforonecountryforallcampaigns/${props.countryName}`}
        target={'_blank'}
        label={'Days'}
      />
      for {props.countryName} for all campaigns
    </div>
  );
};

export default Links;
