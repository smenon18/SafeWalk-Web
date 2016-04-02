function submitform()
{
  var formData = $('#loginForm :input');
  var values = {};
  formData.each(function() {
    values[this.name] = $(this).val();
  });

  values = JSON.stringify(values);

  $.ajax({
    method: 'GET',
    url:'/api/check_login/',
    data: values
  });
}
