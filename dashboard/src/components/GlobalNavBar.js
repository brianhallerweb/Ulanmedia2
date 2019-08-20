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
        to={'/goodwidgets'}
        label={'good widgets'}
      />
    </div>
  );
};

export default GlobalNavBar;
