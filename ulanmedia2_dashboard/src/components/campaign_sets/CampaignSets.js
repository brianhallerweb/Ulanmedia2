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
      Header: '',
      id: 'row',
      Cell: row => <div>{` ${row.index + 1}`}</div>,
      minWidth: 50,
      Footer: <span>{campaignSets.length}</span>,
    },
    {
      Header: 'Vol Campaign ID',
      accessor: 'vol_campaign_id',
      width: 375,
    },
    {Header: 'MGID Campaign ID', accessor: 'mgid_campaign_id', maxwidth: 300},
    {
      Header: 'Campaign Name',
      accessor: 'campaign_name',
      Cell: renderEditable,
      width: 375,
    },
    {
      Header: 'Max Lead CPA',
      accessor: 'max_lead_cpa',
      Cell: renderEditable,
      Footer: (
        <span>
          <strong>Sum:</strong>{' '}
          {_.round(_.sum(_.map(campaignSets, d => d.max_lead_cpa)))}
        </span>
      ),
      maxWidth: 500,
    },
    {
      Header: 'Max Sale CPA',
      accessor: 'max_sale_cpa',
      Cell: renderEditable,
      Footer: (
        <span>
          <strong>Sum:</strong>{' '}
          {_.round(_.sum(_.map(campaignSets, d => d.max_sale_cpa)))}
        </span>
      ),
      maxWidth: 500,
    },
    {
      Header: 'Campaign Status',
      accessor: 'campaign_status',
      Cell: renderEditableDropdown,
      maxWidth: 500,
    },
    {accessor: 'update_button', maxWidth: 500},
    {accessor: 'remove_button', maxWidth: 500},
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
        style={{
          maxHeight: '96vh',
        }}
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
