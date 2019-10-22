//@format
import React, {Component} from 'react';
import ReactTable from 'react-table';
import '../../styles/react-table.css';
import _ from 'lodash';

class CampaignSets extends Component {
  constructor(props) {
    super(props);
    this.state = {
      pageNumber: 0,
      pageSize: 0,
      pageRows: 0,
    };
    this.columns = [
      {
        Header: 'Vol Campaign ID',
        accessor: 'vol_campaign_id',
        width: 375,
      },
      {Header: 'MGID Campaign ID', accessor: 'mgid_campaign_id', maxwidth: 300},
      {
        Header: 'Campaign Name',
        accessor: 'campaign_name',
        Cell: this.renderEditable.bind(this),
        width: 375,
      },
      {
        Header: 'Max Lead CPA',
        accessor: 'max_lead_cpa',
        Cell: this.renderEditable.bind(this),
        Footer: (
          <span>
            <strong>Sum:</strong>{' '}
            {_.round(
              _.sum(_.map(this.props.campaignSets, d => d.max_lead_cpa)),
            )}
          </span>
        ),
        maxWidth: 500,
      },
      {
        Header: 'Max Sale CPA',
        accessor: 'max_sale_cpa',
        Cell: this.renderEditable.bind(this),
        Footer: (
          <span>
            <strong>Sum:</strong>{' '}
            {_.round(
              _.sum(_.map(this.props.campaignSets, d => d.max_sale_cpa)),
            )}
          </span>
        ),
        maxWidth: 500,
      },
      {
        Header: 'Campaign Status',
        accessor: 'campaign_status',
        Cell: this.renderEditableDropdown.bind(this),
        maxWidth: 500,
        sortable: false,
        filterable: false,
      },
      {
        accessor: 'update_button',
        maxWidth: 500,
        sortable: false,
        filterable: false,
      },
      {
        accessor: 'remove_button',
        maxWidth: 500,
        sortable: false,
        filterable: false,
      },
    ];
  }

  renderEditable(cellInfo) {
    return (
      <div
        style={{backgroundColor: '#fafafa'}}
        contentEditable
        suppressContentEditableWarning
        onBlur={e => {
          const data = [...this.props.campaignSets];
          data[cellInfo.index][cellInfo.column.id] = e.target.innerHTML;
        }}
        dangerouslySetInnerHTML={{
          __html: this.props.campaignSets[cellInfo.index][cellInfo.column.id],
        }}
      />
    );
  }

  renderEditableDropdown(cellInfo) {
    return (
      <select
        defaultValue={cellInfo.original.campaign_status}
        onChange={e => {
          const data = [...this.props.campaignSets];
          data[cellInfo.index][cellInfo.column.id] = e.target.value;
        }}>
        <option value="active">Active</option>
        <option value="inactive">Inactive</option>
      </select>
    );
  }

  render() {
    return (
      <div style={{marginTop: 40}}>
        <ReactTable
          filterable
          defaultFilterMethod={(filter, row) =>
            String(row[filter.id]).startsWith(filter.value)
          }
          getPaginationProps={p => {
            let pageNumber = p.page;
            let pageSize = p.pageSize;
            let pageRows = p.pageRows.length;
            if (
              pageNumber !== this.state.pageNumber ||
              pageSize !== this.state.pageSize ||
              pageRows !== this.state.pageRows
            ) {
              this.setState({
                pageNumber: pageNumber,
                pageSize: pageSize,
                pageRows: pageRows,
              });
            }
            return {};
          }}
          style={{
            maxHeight: '96vh',
          }}
          className={'-highlight -striped'}
          columns={this.columns}
          defaultSorted={[
            {
              id: 'campaign_name',
              desc: false,
            },
          ]}
          data={this.props.campaignSets}
          resolveData={data =>
            data.map(row => {
              row['update_button'] = (
                <button onClick={() => this.props.handleUpdateCampaignSet(row)}>
                  Update
                </button>
              );
              row['remove_button'] = (
                <button
                  onClick={() =>
                    this.props.handleDelete(row['vol_campaign_id'])
                  }>
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

        <div style={{textAlign: 'center', paddingTop: 10}}>
          Rows {this.state.pageNumber * this.state.pageSize + 1}-
          {this.state.pageNumber * this.state.pageSize + this.state.pageRows} of{' '}
          {this.props.campaignSets.length}
        </div>
      </div>
    );
  }
}

export default CampaignSets;
