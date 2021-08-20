$(document).ready(function() {
  var blk1 = $('#blk1').DataTable( {
    'columnDefs': [ {
      'targets': [2], 
      'orderable': false, // set orderable false for vud
    }],
  } );
} );