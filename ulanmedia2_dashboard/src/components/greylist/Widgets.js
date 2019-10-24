//@format
import React, {Component} from 'react';
import ReactTable from 'react-table';
import '../../styles/react-table.css';

class Widgets extends Component {
  constructor(props) {
    super(props);
    this.state = {
      pageNumber: 0,
      pageSize: 0,
      pageRows: 0,
    };
    this.columns = [
      {Header: 'Widget ID', accessor: 'widget_id', width: 500},
      {
        Header: 'Domain',
        accessor: 'domain',
        width: 500,
        Cell: rowInfo => (
          <a href={`https://refererhider.com/?http://${rowInfo.row.domain}`}>
            {rowInfo.row.domain}
          </a>
        ),
      },
      {accessor: 'remove_button', width: 500, filterable: false},
    ];
  }

  render() {
    return (
      <div style={{marginTop: 40}}>
        <ReactTable
          filterable
          defaultFilterMethod={(filter, row) =>
            String(row[filter.id]).includes(filter.value)
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
          className={'-highlight -striped'}
          style={{
            maxHeight: '90vh',
          }}
          columns={this.columns}
          data={this.props.widgets}
          resolveData={data => {
            return data.map(row => {
              row['remove_button'] = (
                <button
                  onClick={() => this.props.handleDelete(row['widget_id'])}>
                  Remove
                </button>
              );
              return row;
            });
          }}
          showPageSizeOptions={false}
          defaultPageSize={100}
          minRows={1}
        />

        <div style={{textAlign: 'center', paddingTop: 10}}>
          Rows {this.state.pageNumber * this.state.pageSize + 1}-
          {this.state.pageNumber * this.state.pageSize + this.state.pageRows} of{' '}
          {this.props.widgets.length}
        </div>
      </div>
    );
  }
}

export default Widgets;
