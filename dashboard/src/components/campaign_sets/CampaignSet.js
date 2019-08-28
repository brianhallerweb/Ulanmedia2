//@format
import React from 'react';

const CampaignSet = ({
  index,
  volCampaignID,
  mgidCampaignID,
  campaignName,
  maxLeadCPA,
  maxSaleCPA,
  campaignStatus,
  handleDelete,
  handleRowUpdate,
  handleUpdateCampaignSet,
}) => {
  return (
    <tr key={index}>
      <td>{volCampaignID}</td>
      <td>{mgidCampaignID}</td>
      <td>
        <input
          type="text"
          value={campaignName}
          onChange={e =>
            handleRowUpdate(index, 'campaign_name', e.target.value)
          }
        />
      </td>
      <td>
        <input
          type="text"
          value={maxLeadCPA}
          onChange={e => handleRowUpdate(index, 'max_lead_cpa', e.target.value)}
        />
      </td>
      <td>
        <input
          type="text"
          value={maxSaleCPA}
          onChange={e => handleRowUpdate(index, 'max_sale_cpa', e.target.value)}
        />
      </td>
      <td>
        <select
          defaultValue={campaignStatus}
          onChange={e =>
            handleRowUpdate(index, 'campaign_status', e.target.value)
          }>
          <option value="active">Active</option>
          <option value="inactive">Inactive</option>
        </select>

        {/*<input
          type="text"
          value={campaignStatus}
          onChange={e =>
            handleRowUpdate(index, 'campaign_status', e.target.value)
          }
        /> */}
      </td>
      <td>
        <button
          onClick={() =>
            handleUpdateCampaignSet({
              volCampaignID,
              mgidCampaignID,
              campaignName,
              maxLeadCPA,
              maxSaleCPA,
              campaignStatus,
            })
          }>
          Update
        </button>
      </td>
      <td>
        <button onClick={() => handleDelete(volCampaignID)}>Remove</button>
      </td>
    </tr>
  );
};

export default CampaignSet;
