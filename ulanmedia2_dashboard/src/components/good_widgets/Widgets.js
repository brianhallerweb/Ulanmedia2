//@format
import React from 'react';
import ReactTable from 'react-table';
import 'react-table/react-table.css';

const Widgets = ({widgets, handleDelete}) => {
  const columns = [
    {Header: 'Widget ID', accessor: 'widget_id', width: 500},
    {Header: 'Domain', accessor: 'domain', width: 500},
    {accessor: 'remove_button', width: 500},
  ];

  return (
    <div style={{marginTop: 40}}>
      <ReactTable
        className={'-highlight -striped'}
        columns={columns}
        data={widgets}
        resolveData={data =>
          data.map(row => {
            row['remove_button'] = (
              <button onClick={() => handleDelete(row['widget_id'])}>
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

export default Widgets;
