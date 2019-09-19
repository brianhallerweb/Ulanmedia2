//@format
import React from 'react';
import WidgetDomain from './WidgetDomain';
import ReactTable from 'react-table';
import 'react-table/react-table.css';

const WidgetDomains = ({widgetDomains, handleDelete}) => {
  const columns = [
    {Header: 'Traffic Source', accessor: 'traffic_source', maxwidth: 500},
    {Header: 'Widget ID', accessor: 'widget_id', maxwidth: 500},
    {Header: 'Domain', accessor: 'domain', maxwidth: 500},
    {
      Header: 'Widget Domain Source',
      accessor: 'widget_domain_source',
      maxwidth: 500,
    },
    {accessor: 'remove_button', maxwidth: 500},
  ];

  return (
    <div style={{marginTop: 40}}>
      <ReactTable
        className={'-highlight -striped'}
        columns={columns}
        data={widgetDomains}
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
        showPaginationTop={true}
        showPaginationBottom={false}
        showPageSizeOptions={false}
        defaultPageSize={100}
        minRows={1}
      />
    </div>
  );
};

export default WidgetDomains;
