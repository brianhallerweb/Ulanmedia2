//@format
import React from 'react';
import InternalLink from '../utilities/InternalLink';

const Links = props => {
  return (
    <div>
      <InternalLink
        className={'rowLink'}
        stopPropagation={true}
        to={`/monthsforoneofferforallcampaigns/${props.offerName}`}
        target={'_blank'}
        label={'Months'}
      />
      <InternalLink
        className={'rowLink'}
        stopPropagation={true}
        to={`/daysforoneofferforallcampaigns/${props.offerName}`}
        target={'_blank'}
        label={'Days'}
      />
      for {props.offerName} for all campaigns
    </div>
  );
};

export default Links;
