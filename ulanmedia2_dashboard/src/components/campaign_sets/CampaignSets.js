//@format
import React from 'react';
import CampaignSet from './CampaignSet';

const CampaignSets = ({
  campaignSets,
  handleDelete,
  handleRowUpdate,
  handleUpdateCampaignSet,
}) => {
  return (
    <table style={{marginTop: 30, width: '50%'}}>
      <thead>
        <tr>
          <th>Vol Campaign ID</th>
          <th>Mgid Campaign ID</th>
          <th>Campaign Name</th>
          <th>Max Lead CPA</th>
          <th>Max Sale CPA</th>
          <th>Campaign Status</th>
          <th />
          <th />
        </tr>
      </thead>
      <tbody>
        {campaignSets.map((campaignSet, index) => (
          <CampaignSet
            key={index}
            index={index}
            volCampaignID={campaignSet.vol_campaign_id}
            mgidCampaignID={campaignSet.mgid_campaign_id}
            campaignName={campaignSet.campaign_name}
            maxLeadCPA={campaignSet.max_lead_cpa}
            maxSaleCPA={campaignSet.max_sale_cpa}
            campaignStatus={campaignSet.campaign_status}
            handleDelete={handleDelete}
            handleRowUpdate={handleRowUpdate}
            handleUpdateCampaignSet={handleUpdateCampaignSet}
          />
        ))}
      </tbody>
    </table>
  );
};

export default CampaignSets;
