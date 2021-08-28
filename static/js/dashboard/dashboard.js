function updateTooltip(code_edit_id,btn_copy_id) {
  document.getElementById(btn_copy_id).title = "Copied: " + document.getElementById(code_edit_id).value;
}

$.fn.modal.Constructor.prototype._enforceFocus = function() {};

function disableBeforeToday(input_date_id) {
  var dateToday = new Date().toISOString().slice(0, 10);
  document.getElementById(input_date_id).setAttribute("min",dateToday);
}

$(document).ready(function() {
  var createdDataTable = $('#createdDataTable').DataTable( {
    'columnDefs': [ {
      'targets': [2], 
      'orderable': false, // set orderable false for vud
    }],
  } );
  var joinedDataTable = $('#joinedDataTable').DataTable( {
    'columnDefs': [ {
      'targets': [2], 
      'orderable': false, // set orderable false for vud
    }],
  } );

  new ClipboardJS('.copy-to-clipboard');

} );