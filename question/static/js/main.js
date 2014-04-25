$(document).ready(function() {
      $(document).foundation();
var removeSubmit = function  () {
  $('#submit').remove();
};
var addSubmit = function() {
  var text = '<li><span class="label" id="submit">Submit</span></li>';
  $('#ctrl').append(text);
  $('#submit').click(function() {
    var text = $('#question textarea').val();
    var el = $('#ctrl');
    var url =  el.attr('href');
    var id = el.attr('pk')
    removeSubmit();
    console.log(url, id, text);
    $.ajax({
              beforeSend: function(xhr, settings) {
                      xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
              },
              data: {},
              type: 'POST',
              url: url,
              success: function(response) {
                  console.log(JSON.stringify(response));
              }
          });
  });
};

var addClose = function() {
  $('#edit').click(function() {
    var q = $('#question div label');
    q.html('<textarea rows=10> ' + q.text() + '</textarea>');
    $('#edit').text('Close');
    var edit = $('#edit');
    edit.off('click');

    edit.attr('id', "close");
    addSubmit();
    addEdit();
  });
  
};

var send_message= function(text){
  var m = $('#messages');
  var text ='<div data-alert="" class="alert-box message.tags radius">'+  text + '<a href="#" class="close">×</a></div>';
  m.append(text);
  Foundation.libs.alert.init();
};

    


var addEdit = function() {
  $('#close').click(function() {
    var text = $('#question textarea').val();
    var label = $('#question label');
    label.html(text);
    close = $('#close');
    close.text('Edit');
    close.off('click');
    close.attr('id', "edit");
    removeSubmit();
    send_message('Request sended');
    addClose();
  });
  
};






$('a.reveal').click(function(event) {
  event.preventDefault();
  var $div = $('<div>').addClass('reveal-modal').appendTo('body'),
    $this = $(this);
  $.get($this.attr('href'), function(data) {
    console.log(data);
    return $div.empty().html(data).append('<a class="close-reveal-modal">&#215;</a>').reveal();
  });
});
      $('#form').submit(function() {
          $.ajax({
              beforeSend: function(xhr, settings) {
                      xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
              },
              data: $(this).serialize(),
              type: 'POST',
              url: $(this).attr('action'),
              success: function(response) {
                  console.log(JSON.stringify(response));
              }
          });
          return false;
      });
  });