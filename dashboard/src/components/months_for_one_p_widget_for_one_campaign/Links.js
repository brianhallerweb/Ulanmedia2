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
      </div>

      <div>
        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/monthsforonepwidgetforonecampaign/${props.pWidgetID}/${
            props.volID
          }/${props.name}/`}
          target={'_blank'}
          label={'Months'}
        />
        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/daysforonepwidgetforonecampaign/${props.pWidgetID}/${
            props.volID
          }/${props.name}/`}
          target={'_blank'}
          label={'Days'}
        />
        for {props.pWidgetID} for {props.name}
      </div>
      <div style={{marginTop: 10}}>
        <InternalLink
          className={'rowLink'}
          to={`/excludecampaignforonepwidgetconfirmation/${props.pWidgetID}/${
            props.mgidID
          }`}
          target={'_blank'}
          label={'exclude p widget from campaign'}
        />
      </div>
    </div>
  );
};

export default Links;
