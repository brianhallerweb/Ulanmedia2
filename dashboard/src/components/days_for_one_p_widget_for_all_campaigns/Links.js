//@format
import React from 'react';
import InternalLink from '../utilities/InternalLink';

const Links = props => {
  return (
    <div>
      <InternalLink
        className={'rowLink'}
        stopPropagation={true}
        to={`/monthsforonepwidgetforallcampaigns/${props.pWidgetID}`}
        target={'_blank'}
        label={'Months'}
      />
      <InternalLink
        className={'rowLink'}
        stopPropagation={true}
        to={`/daysforonepwidgetforallcampaigns/${props.pWidgetID}`}
        target={'_blank'}
        label={'Days'}
      />
      for {props.pWidgetID} for all campaigns
      <div style={{marginTop: 10}}>
        <InternalLink
          className={'rowLink'}
          to={`/excludepwidgetconfirmation/${props.pWidgetID}`}
          target={'_blank'}
          label={'exclude p widget from all campaigns'}
        />
      </div>
    </div>
  );
};

export default Links;
