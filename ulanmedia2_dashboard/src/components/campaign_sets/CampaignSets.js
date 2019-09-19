//@format
import React from 'react';
import ReactTable from 'react-table';
import 'react-table/react-table.css';

const CampaignSets = ({
  campaignSets,
  handleDelete,
  handleRowUpdate,
  handleUpdateCampaignSet,
}) => {
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
      Cell: renderEditable,
      maxwidth: 500,
    },
    {
      Header: 'Max Lead CPA',
      accessor: 'max_lead_cpa',
      Cell: renderEditable,
      maxwidth: 500,
    },
    {
      Header: 'Max Sale CPA',
      accessor: 'max_sale_cpa',
      Cell: renderEditable,
      maxwidth: 500,
    },
    {
      Header: 'Campaign Status',
      accessor: 'campaign_status',
      Cell: renderEditable,
      maxwidth: 500,
    },
    {accessor: 'update_button', maxwidth: 500},
    {accessor: 'remove_button', maxwidth: 500},
  ];

  function renderEditable(cellInfo) {
    return (
      <div
        style={{backgroundColor: '#fafafa'}}
        contentEditable
        suppressContentEditableWarning
        onBlur={e => {
          const data = [...campaignSets];
          data[cellInfo.index][cellInfo.column.id] = e.target.innerHTML;
          //this.setState({data});
        }}
        dangerouslySetInnerHTML={{
          __html: campaignSets[cellInfo.index][cellInfo.column.id],
        }}
      />
    );
  }

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
              <button onClick={() => handleUpdateCampaignSet(row)}>
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
