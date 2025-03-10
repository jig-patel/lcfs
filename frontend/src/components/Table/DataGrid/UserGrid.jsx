// GridExample.js
import React, { useMemo, useEffect, useState } from 'react';
import { AgGridReact } from '@ag-grid-community/react';
import { ClientSideRowModelModule } from '@ag-grid-community/client-side-row-model';
import '@ag-grid-community/styles/ag-grid.css';
import '@ag-grid-community/styles/ag-theme-alpine.css';
import { ModuleRegistry } from '@ag-grid-community/core';
import StatusRenderer from './StatusRenderer';

ModuleRegistry.registerModules([ClientSideRowModelModule]);

const UserGrid = (props) => {
  const sideBar = useMemo(() => {
    toolPanels: ['filters', 'columns']
  }, []);

  const columnDefs = useMemo(() => [
    { field: 'name', editable: true },
    { field: 'role', headerName: 'Role(s)' },
    { field: 'email' },
    { field: 'phone' },
    {
      field: 'status',
      filter: 'agSetColumnFilter',
      filterParams: {
        values: ['Active', 'Inactive'],
        buttons: ['apply', 'reset'],
        filterOptions: ['equals'],
        defaultOption: 'equals',
        closeOnApply: true,
        suppressAndOrCondition: true,
        applyMiniFilterWhileTyping: true,
      },
      filter: true,
      cellRenderer: StatusRenderer,
    },
  ], []);

  // never changes, so we can use useMemo
  const defaultColDef = useMemo(() => ({
    // flex: 1,
    resizable: true,
    sortable: true,
    filter: true,
    floatingFilter: true,
    // filterParams: {
    //   buttons: ['apply', 'reset'],
    //   closeOnApply: true,
    // }
  }), []);

  const [rowData, setRowData] = useState();

  useEffect(() => {
    // fetch('https://www.ag-grid.com/example-assets/olympic-winners.json')
    //   .then(resp => resp.json())
    //   .then(data => setRowData(data));
    setRowData([...props.rows])
  }, []);

  return (
    <div className="ag-theme-alpine" style={{ width: '100%', height: '100%' }}>
      <AgGridReact
        className="ag-theme-alpine"
        animateRows="true"
        columnDefs={columnDefs}
        defaultColDef={defaultColDef}
        enableRangeSelection="true"
        rowData={rowData}
        rowSelection="multiple"
        suppressRowClickSelection="true"
        pagination
        paginationPageSize={10}
        domLayout='autoHeight'
        sideBar={sideBar}
      />
    </div>
  );
};

export default UserGrid;
