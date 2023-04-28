const ur ='https://stefanbohacek.com/hellosalut/?lang=fr';
$(() => {
  $.getJSON(ur, (data) => {
    var hello = $(data).find('#hello').text();
    $('DIV#hello').text(hello);
  });
});
//$('ul.my_list').append('<li>Item</li>');