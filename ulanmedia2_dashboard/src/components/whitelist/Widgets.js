//@format
import React, {Component} from 'react';
import Widget from './Widget';
import ReactTable from 'react-table';
import 'react-table/react-table.css';

const Widgets = ({widgets, handleDelete}) => {
  const columns = [
    {Header: 'Widget ID', accessor: 'widget_id', width: 500},
    {Header: 'test column', accessor: 'widget_id', width: 500},
  ];
  return (
    <div style={{marginTop: 40}}>
      <ReactTable
        className={'-highlight -striped'}
        columns={columns}
        data={widgets}
        showPaginationTop={true}
        showPaginationBottom={false}
        showPageSizeOptions={false}
        defaultPageSize={100}
        minRows={1}
      />
    </div>
  );
};

//const Widgets = ({widgets, handleDelete}) => {
//console.log(widgets);
//return (
//<table style={{marginTop: 30, width: '50%'}}>
//<thead>
//<tr>
//<th>Widget ID</th>
//<th />
//</tr>
//</thead>
//<tbody>
//{widgets.map(widget => (
//<Widget
//key={widget.widget_id}
//widgetID={widget.widget_id}
//handleDelete={handleDelete}
///>
//))}
//</tbody>
//</table>
//);
//};

export default Widgets;
