//@format
import React from 'react';
import {NavLink} from 'react-router-dom';
import InternalLink from './utilities/InternalLink';
import ExternalLink from './utilities/ExternalLink';

const GlobalNavBar = () => {
  const dates = calculateOneEightyDateRange();
  const startDate = dates[0];
  const endDate = dates[1];

  const deviceOSBrowserURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_3e70ca4d-5ccb-49c3-ab23-e2bc652fbbc9/report/device,os,browser?dateRange=custom-date&sortKey=profit&sortDirection=desc&page=1&chart=0&columns=deviceName&columns=os&columns=browser&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=1000&reportType=tree&include=ALL&reportDataType=0&tagsGrouping=device&valueFiltersGrouping=device&from=${startDate}T00:00:00Z&to=${endDate}T00:00:00Z&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc`;

  const ISPURL =
    'https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_3e70ca4d-5ccb-49c3-ab23-e2bc652fbbc9/report/isp,custom-variable-1?dateRange=last-30-days&sortKey=profit&sortDirection=asc&page=1&chart=0&columns=isp&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=1000&reportType=tree&include=ALL&reportDataType=0&tagsGrouping=isp&valueFiltersGrouping=isp&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc';

  const monthsURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_e9930901-c292-4dcf-b73a-d5eb6c44bac1/report/month?dateRange=custom-date&sortKey=month&sortDirection=asc&page=1&chart=0&columns=month&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=100&reportType=&include=ACTIVE&reportDataType=0&tagsGrouping=month&valueFiltersGrouping=month&from=${startDate}T00:00:00Z&to=${endDate}T00:00:00Z&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc`;

  const daysURL =
    'https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_e9930901-c292-4dcf-b73a-d5eb6c44bac1/report/day?dateRange=last-30-days&sortKey=day&sortDirection=desc&page=1&chart=0&columns=day&columns=visits&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=100&reportType=&include=ACTIVE&reportDataType=0&tagsGrouping=day&valueFiltersGrouping=day&from=2018-05-28T00:00:00Z&to=2018-06-27T00:00:00Z&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc';

  return (
    <div className="globalNavBar">
      <InternalLink
        className={'globalNavItem'}
        activeClassName={'is-active'}
        to={'/campaignsforallcampaigns'}
        label={'campaigns'}
      />

      <InternalLink
        className={'globalNavItem'}
        activeClassName={'is-active'}
        to={'/pwidgetsforallcampaigns'}
        label={'p widgets'}
      />

      <InternalLink
        className={'globalNavItem'}
        activeClassName={'is-active'}
        to={'/cwidgetsforallcampaigns'}
        label={'c widgets'}
      />

      <InternalLink
        className={'globalNavItem'}
        activeClassName={'is-active'}
        to={'/offersforallcampaigns'}
        label={'offers'}
      />

      <InternalLink
        className={'globalNavItem'}
        activeClassName={'is-active'}
        to={'/adsforallcampaigns'}
        label={'ads'}
      />

      <InternalLink
        className={'globalNavItem'}
        activeClassName={'is-active'}
        to={'/countriesforallcampaigns'}
        label={'countries'}
      />

      <InternalLink
        className={'globalNavItem'}
        activeClassName={'is-active'}
        to={'/languagesforallcampaigns'}
        label={'languages'}
      />

      <ExternalLink
        className={'globalNavItem'}
        target={'_blank'}
        href={deviceOSBrowserURL}
        label={'device/os/browser'}
      />

      <ExternalLink
        className={'globalNavItem'}
        target={'_blank'}
        href={ISPURL}
        label={'isp'}
      />

      <ExternalLink
        className={'globalNavItem'}
        target={'_blank'}
        href={monthsURL}
        label={'months'}
      />

      <ExternalLink
        className={'globalNavItem'}
        target={'_blank'}
        href={daysURL}
        label={'days'}
      />

      <InternalLink
        className={'globalNavItem'}
        activeClassName={'is-active'}
        to={'/campaignsforgoodpwidgets'}
        target={'_blank'}
        label={'good p widgets'}
      />

      <InternalLink
        className={'globalNavItem'}
        activeClassName={'is-active'}
        to={'/excludeonecampaignforallblacklistedpandcwidgets'}
        target={'_blank'}
        label={'exclude new campaign from all blacklisted widgets'}
      />

      <InternalLink
        className={'globalNavItem'}
        activeClassName={'is-active'}
        to={'/updatealldata'}
        target={'_blank'}
        label={'update all data'}
      />

      <InternalLink
        className={'globalNavItem'}
        activeClassName={'is-active'}
        to={'/updateoneeightydata'}
        target={'_blank'}
        label={'update one eighty data'}
      />
    </div>
  );
};

const moment = require('moment-timezone');

function calculateOneEightyDateRange() {
  const today = moment()
    .tz('America/Los_Angeles')
    .format('YYYY-MM-DD');
  const oneEightyDaysAgo = moment()
    .tz('America/Los_Angeles')
    .subtract(180, 'day')
    .format('YYYY-MM-DD');
  return [oneEightyDaysAgo, today];
}

export default GlobalNavBar;
