//@format
import React, {Component} from 'react';
import ReactTable from 'react-table';
import '../../styles/react-table.css';

class WidgetDomains extends Component {
  constructor(props) {
    super(props);
    this.state = {
      pageNumber: 0,
      pageSize: 0,
      pageRows: 0,
    };
    this.columns = [
      {Header: 'Traffic Source', accessor: 'traffic_source', maxWidth: 500},
      {Header: 'Widget ID', accessor: 'widget_id', maxWidth: 500},
      {
        Header: 'Domain',
        accessor: 'domain',
        maxWidth: 500,
        Cell: rowInfo => (
          <a href={`https://refererhider.com/?http://${rowInfo.row.domain}`}>
            {rowInfo.row.domain}
          </a>
        ),
      },
      {
        Header: 'Widget Domain Source',
        accessor: 'widget_domain_source',
        maxwidth: 500,
      },
      {
        accessor: 'remove_button',
        maxWidth: 500,
        sortable: false,
        filterable: false,
      },
    ];
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
          data={this.props.widgetDomains}
          resolveData={data =>
            data.map(row => {
              row['remove_button'] = (
                <button
                  onClick={() =>
                    handleDelete(
                      row['traffic_source'],
                      row['widget_id'],
                      row['domain'],
                      row['widget_domain_source'],
                    )
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
          defaultSorted={[
            {
              id: 'domain',
              desc: false,
            },
          ]}
        />

        <div style={{textAlign: 'center', paddingTop: 10}}>
          Rows {this.state.pageNumber * this.state.pageSize + 1}-
          {this.state.pageNumber * this.state.pageSize + this.state.pageRows} of{' '}
          {this.props.widgetDomains.length}
        </div>
      </div>
    );
  }
}

export default WidgetDomains;
