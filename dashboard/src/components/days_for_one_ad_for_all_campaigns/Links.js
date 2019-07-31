//@format
import React from 'react';
import InternalLink from '../utilities/InternalLink';

const Links = props => {
  return (
    <div>
      <InternalLink
        className={'rowLink'}
        stopPropagation={true}
        to={`/monthsforoneadforallcampaigns/${props.adImage}`}
        target={'_blank'}
        label={'Months'}
      />
      <InternalLink
        className={'rowLink'}
        stopPropagation={true}
        to={`/daysforoneadforallcampaigns/${props.adImage}`}
        target={'_blank'}
        label={'Days'}
      />
      for {props.adImage} for all campaigns
    </div>
  );
};

export default Links;
