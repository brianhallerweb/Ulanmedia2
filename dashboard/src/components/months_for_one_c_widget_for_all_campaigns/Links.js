//@format
import React from 'react';
import InternalLink from '../utilities/InternalLink';

const Links = props => {
  return (
    <div>
      <div>
        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/monthsforonepwidgetforallcampaigns/${props.cWidgetID.match(
            /^\d*/,
          )}`}
          target={'_blank'}
          label={'Months'}
        />
        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/daysforonepwidgetforallcampaigns/${props.cWidgetID.match(
            /^\d*/,
          )}`}
          target={'_blank'}
          label={'Days'}
        />
        for {props.cWidgetID.match(/^\d*/)} for all campaigns
      </div>
      <div>
        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/monthsforonecwidgetforallcampaigns/${props.cWidgetID}`}
          target={'_blank'}
          label={'Months'}
        />
        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/daysforonecwidgetforallcampaigns/${props.cWidgetID}`}
          target={'_blank'}
          label={'Days'}
        />
        for {props.cWidgetID} for all campaigns
      </div>
    </div>
  );
};

export default Links;
