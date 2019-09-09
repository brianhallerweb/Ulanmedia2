//@format
import React from 'react';
import {NavLink} from 'react-router-dom';
import InternalLink from './utilities/InternalLink';

const GlobalNavBar = () => {
  return (
    <div className="globalNavBar">
      <InternalLink
        className={'globalNavItem'}
        activeClassName={'is-active'}
        to={'/whitelist'}
        label={'white'}
      />
      <InternalLink
        className={'globalNavItem'}
        activeClassName={'is-active'}
        to={'/greylist'}
        label={'grey'}
      />
      <InternalLink
        className={'globalNavItem'}
        activeClassName={'is-active'}
        to={'/blacklist'}
        label={'black'}
      />
      <InternalLink
        className={'globalNavItem'}
        activeClassName={'is-active'}
        to={'/goodwidgets'}
        label={'good widgets'}
      />
      <InternalLink
        className={'globalNavItem'}
        activeClassName={'is-active'}
        to={'/campaignsets'}
        label={'campaign sets'}
      />
      <InternalLink
        className={'globalNavItem'}
        activeClassName={'is-active'}
        to={'/widgetdomains'}
        label={'widget-domains'}
      />
    </div>
  );
};

export default GlobalNavBar;
