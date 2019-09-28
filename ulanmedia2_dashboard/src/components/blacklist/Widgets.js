//@format
import React from 'react';
import ReactTable from 'react-table';
import '../../styles/react-table.css';

const Widgets = ({widgets, handleDelete}) => {
  const columns = [
    {
      Header: '',
      id: 'row',
      Cell: row => <div>{` ${row.index + 1}`}</div>,
      minWidth: 50,
      Footer: <span>{widgets.length}</span>,
    },
    {Header: 'Widget ID', accessor: 'widget_id', width: 500},
    {Header: 'Domain', accessor: 'domain', width: 500},
    {accessor: 'remove_button', width: 500},
  ];

  return (
    <div style={{marginTop: 40}}>
      <ReactTable
        className={'-highlight -striped'}
        style={{
          maxHeight: '96vh',
        }}
        columns={columns}
        data={widgets}
        resolveData={data =>
          data.map(row => {
            const domain = row['domain'];
            row['domain'] = (
              <a href={`https://refererhider.com/?http://${domain}`}>
                {domain}
              </a>
            );

            row['remove_button'] = (
              <button onClick={() => handleDelete(row['widget_id'])}>
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

export default Widgets;
