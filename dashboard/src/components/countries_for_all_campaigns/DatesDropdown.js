//@format
import React, {Component} from 'react';
import {NavLink} from 'react-router-dom';

const DatesDropdown = ({selectDateRange, dateRange}) => (
  <div>
    <span>Date range </span>
    <select
      onChange={e => selectDateRange(e.target.value)}
      defaultValue={dateRange}>
      <option value="yesterday">Yesterday</option>
      <option value="seven">7 days</option>
      <option value="thirty">30 days</option>
      <option value="ninety">90 days</option>
      <option value="oneeighty">180 days</option>
    </select>
  </div>
);

export default DatesDropdown;
