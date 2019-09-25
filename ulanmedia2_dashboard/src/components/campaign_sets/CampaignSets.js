//@format
import React from 'react';
import ReactTable from 'react-table';
import '../../styles/react-table.css';
import _ from 'lodash';

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
      Header: (
        <span>
          <strong>Sum:</strong>{' '}
          {_.round(_.sum(_.map(campaignSets, d => d.max_lead_cpa)))}
        </span>
      ),
      maxwidth: 500,
      columns: [
        {
          Header: 'Max Lead CPA',
          accessor: 'max_lead_cpa',
          Cell: renderEditable,
          maxwidth: 500,
        },
      ],
    },
    {
      Header: (
        <span>
          <strong>Sum:</strong>{' '}
          {_.round(_.sum(_.map(campaignSets, d => d.max_sale_cpa)))}
        </span>
      ),
      maxwidth: 500,
      columns: [
        {
          Header: 'Max Sale CPA',
          accessor: 'max_sale_cpa',
          Cell: renderEditable,
          maxwidth: 500,
        },
      ],
    },
    {
      Header: 'Campaign Status',
      accessor: 'campaign_status',
      Cell: renderEditableDropdown,
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

  function renderEditableDropdown(cellInfo) {
    return (
      <select
        defaultValue={cellInfo.original.campaign_status}
        onChange={e => {
          const data = [...campaignSets];
          data[cellInfo.index][cellInfo.column.id] = e.target.value;
        }}>
        <option value="active">Active</option>
        <option value="inactive">Inactive</option>
      </select>
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
            row['update_button'] = (
              <button onClick={() => handleUpdateCampaignSet(row)}>
                Update
              </button>
            );
            row['remove_button'] = (
              <button onClick={() => handleDelete(row['vol_campaign_id'])}>
                Remove
              </button>
            );
            return row;
          })
        }
        showPageSizeOptions={false}
        defaultPageSize={100}
        minRows={1}
      />
    </div>
  );
};

export default CampaignSets;
