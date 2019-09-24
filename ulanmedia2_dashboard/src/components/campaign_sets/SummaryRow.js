//@format
import React from 'react';
import ReactTable from 'react-table';
import 'react-table/react-table.css';

const SummaryRow = ({campaignSets}) => {
  let summaryRow = {
    vol_campaign_id: '',
    mgid_campaign_id: '',
    campaign_name: '',
    max_lead_cpa: 0,
    max_sale_cpa: 0,
    campaign_status: '',
  };

  for (let campaignSet in campaignSets) {
    summaryRow['max_lead_cpa'] += campaignSets[campaignSet]['max_lead_cpa'];
    summaryRow['max_sale_cpa'] += campaignSets[campaignSet]['max_sale_cpa'];
  }

  const columns = [
    {
      Header: 'Vol Campaign ID',
      accessor: 'vol_campaign_id',
      maxwidth: 500,
    },
    {Header: 'MGID Campaign ID', accessor: 'mgid_campaign_id', maxwidth: 500},
    {
      Header: 'Campaign Name',
      accessor: 'campaign_name',
      maxwidth: 500,
    },
    {
      Header: 'Max Lead CPA',
      accessor: 'max_lead_cpa',
      maxwidth: 500,
    },
    {
      Header: 'Max Sale CPA',
      accessor: 'max_sale_cpa',
      maxwidth: 500,
    },
    {
      Header: 'Campaign Status',
      accessor: 'campaign_status',
      maxwidth: 500,
    },
  ];

  return (
    <div style={{marginTop: 30, marginBottom: 40}}>
      Summary Row
      <ReactTable
        columns={columns}
        data={[summaryRow]}
        showPageSizeOptions={false}
        showPaginationBottom={false}
        minRows={1}
      />
    </div>
  );
};

export default SummaryRow;
