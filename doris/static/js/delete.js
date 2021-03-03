$('#deleteModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var recipient = button.data('r') // Extract info from data-* attributes
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content.
  $('#deleteModalAction').on('click', function(event) {
    alert('delete ' + button.data('delete-url'))
  })
  $('#deleteModalText').text(button.data('delete-text'))
})
