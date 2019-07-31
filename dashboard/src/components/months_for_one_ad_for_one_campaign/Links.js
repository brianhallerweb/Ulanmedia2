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
          to={`/monthsforoneadforallcampaigns/${props.adImage}/`}
          target={'_blank'}
          label={'Months'}
        />
        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/daysforoneadforallcampaigns/${props.adImage}/`}
          target={'_blank'}
          label={'Days'}
        />
        for {props.adImage} for all campaigns
      </div>

      <div>
        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/monthsforoneadforonecampaign/${props.adImage}/${props.volID}/${
            props.name
          }/`}
          target={'_blank'}
          label={'Months'}
        />
        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/daysforoneadforonecampaign/${props.adImage}/${props.volID}/${
            props.name
          }/`}
          target={'_blank'}
          label={'Days'}
        />
        for {props.adImage} for {props.name}
      </div>
    </div>
  );
};

export default Links;
