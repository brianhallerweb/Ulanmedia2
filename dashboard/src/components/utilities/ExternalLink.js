//@format
import React, {Component} from 'react';

const ExternalLink = ({className, href, target, label}) => (
  <div className={className}>
    <a onClick={e => e.stopPropagation()} href={href} target={target}>
      {label}
    </a>
  </div>
);

export default ExternalLink;
