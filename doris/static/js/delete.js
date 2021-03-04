$('#deleteModal').on('show.bs.modal', function (event) {
  var deleteModal = $('#deleteModal')
  var button = $(event.relatedTarget) // Button that triggered the modal
  var recipient = button.data('r') // Extract info from data-* attributes
  $('#deleteModalAction').on('click', function(event) {
    $.ajax({
      url: button.data('delete-url'),
      type: 'DELETE',
      success: function(result) {
        window.location.replace('/')
      },
      error: function(result, error, status) {
        deleteModal.modal('hide')
        var confirmModal = $('#confirmModal')
        confirmModal.addClass('alert-danger')
        confirmModal.find('p').text('Failed: ' + status)
        confirmModal.addClass('show')
        confirmModal.alert()
      }
    });
  })
  $('#deleteModalText').text(button.data('delete-text'))
})
