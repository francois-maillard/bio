$('#deleteModal').on('show.bs.modal', function (event) {
  var deleteModal = $('#deleteModal')
  var button = $(event.relatedTarget) // Button that triggered the modal
  var recipient = button.data('r') // Extract info from data-* attributes
  $('#deleteModalAction').on('click', function(event) {
    $.ajax({
      url: button.data('delete-url'),
      type: 'DELETE',
      success: function(result) {
        window.location.replace(button.data('reload-url'))
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

$('.btn-thumbnail').on('click', function(event) {
  var button = $(this) // Button that triggered the modal
  $.ajax({
    url: button.data('url'),
    type: 'POST',
    dataType: "json",
    data: JSON.stringify({'photo_id': button.data('photo-id')}),
    contentType: "application/json; charset=utf-8",
    success: function(result) {
      var confirmModal = $('#confirmModal')
      confirmModal.addClass('alert-success')
      confirmModal.find('p').text('Thumbnail updated')
      confirmModal.addClass('show')
      confirmModal.alert()
    },
    error: function(result, error, status) {
      var confirmModal = $('#confirmModal')
      confirmModal.addClass('alert-danger')
      confirmModal.find('p').text('Failed: ' + status)
      confirmModal.addClass('show')
      confirmModal.alert()
    }
  });
})

$('.btn-tag').on('change', function(event) {
  var input = $(this) // Button that triggered the modal
  var url = location.pathname + '?';
  input.closest('.btn-group').find(':checked').each(function () {
    var tag_input = $(this);
    url = url + 'tags=' + tag_input.attr('data-tag-id') + '&';
  });
  window.location.href = url;
})

$('.btn-add-tag').on('click', function(event) {
  var button = $(this) // Button that triggered the modal
  var input = $('#add-tag');
  $.ajax({
    url: button.data('url'),
    type: 'POST',
    dataType: "json",
    data: JSON.stringify({'tag': $('#add-tag').val()}),
    contentType: "application/json; charset=utf-8",
    success: function(result) {
      window.location.reload();
    },
    error: function(result, error, status) {
      var confirmModal = $('#confirmModal')
      confirmModal.addClass('alert-danger')
      confirmModal.find('p').text('Failed: ' + status)
      confirmModal.addClass('show')
      confirmModal.alert()
    }
  });
})

$('.btn-delete-tag').on('click', function(event) {
  var button = $(this) // Button that triggered the modal
  $.ajax({
    url: button.data('url'),
    type: 'DELETE',
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    success: function(result) {
      window.location.reload();
    },
    error: function(result, error, status) {
      var confirmModal = $('#confirmModal')
      confirmModal.addClass('alert-danger')
      confirmModal.find('p').text('Failed: ' + status)
      confirmModal.addClass('show')
      confirmModal.alert()
    }
  });
})

