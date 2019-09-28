//@format
import React from 'react';
import ReactTable from 'react-table';
import '../../styles/react-table.css';

const WidgetDomains = ({widgetDomains, handleDelete}) => {
  const columns = [
    {
      Header: '',
      id: 'row',
      Cell: row => <div>{` ${row.index + 1}`}</div>,
      minWidth: 50,
      Footer: <span>{widgetDomains.length}</span>,
    },
    {Header: 'Traffic Source', accessor: 'traffic_source', maxWidth: 500},
    {Header: 'Widget ID', accessor: 'widget_id', maxWidth: 500},
    {Header: 'Domain', accessor: 'domain', maxWidth: 500},
    {
      Header: 'Widget Domain Source',
      accessor: 'widget_domain_source',
      maxwidth: 500,
    },
    {accessor: 'remove_button', maxWidth: 500},
  ];

  return (
    <div style={{marginTop: 40}}>
      <ReactTable
        style={{
          maxHeight: '96vh',
        }}
        className={'-highlight -striped'}
        columns={columns}
        data={widgetDomains}
        resolveData={data =>
          data.map(row => {
            const domain = row['domain'];
            row['domain'] = (
              <a href={`https://refererhider.com/?http://${domain}`}>
                {domain}
              </a>
            );
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
      />
    </div>
  );
};

export default WidgetDomains;
