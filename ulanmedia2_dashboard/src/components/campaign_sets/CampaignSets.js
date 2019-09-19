//@format
import React from 'react';
//import CampaignSet from './CampaignSet';
import ReactTable from 'react-table';
import 'react-table/react-table.css';

const CampaignSets = ({
  campaignSets,
  handleDelete,
  handleRowUpdate,
  handleUpdateCampaignSet,
}) => {
  const columns = [
    {Header: 'Vol Campaign ID', accessor: 'vol_campaign_id', maxwidth: 500},
    {Header: 'MGID Campaign ID', accessor: 'mgid_campaign_id', maxwidth: 500},
    {Header: 'Campaign Name', accessor: 'campaign_name', maxwidth: 500},
    {Header: 'Max Lead CPA', accessor: 'max_lead_cpa', maxwidth: 500},
    {Header: 'Max Sale CPA', accessor: 'max_sale_cpa', maxwidth: 500},
    {Header: 'Max Sale CPA', accessor: 'max_sale_cpa', maxwidth: 500},
    {Header: 'Campaign Status', accessor: 'campaign_status', maxwidth: 500},
    {accessor: 'update_button', maxwidth: 500},
    {accessor: 'remove_button', maxwidth: 500},
  ];

  return (
    <div style={{marginTop: 40}}>
      <ReactTable
        className={'-highlight -striped'}
        columns={columns}
        data={campaignSets}
        resolveData={data =>
          data.map(row => {
            row['remove_button'] = (
              <button onClick={() => handleDelete(row['vol_campaign_id'])}>
                Remove
              </button>
            );
            row['update_button'] = (
              <button
                onClick={() =>
                  handleUpdateCampaignSet(
                    row['vol_campaign_id'],
                    row['mgid_campaign_id'],
                    row['campaign_name'],
                    row['max_lead_cpa'],
                    row['max_sale_cpa'],
                    row['campaign_status'],
                  )
                }>
                {' '}
                Update
              </button>
            );
            return row;
          })
        }
        showPaginationTop={true}
        showPaginationBottom={false}
        showPageSizeOptions={false}
        defaultPageSize={100}
        minRows={1}
      />
    </div>
  );
};

export default CampaignSets;
