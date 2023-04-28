const ur = 'https://swapi-api.hbtn.io/api/films/?format=json';
$(() => {
  $.getJSON(ur, (data) => {
    for (let i = 0; i < data.results.length; i++){
    const lst_item = $('<li></li>').text(data.results[i].title);
    $('UL#list_movies').append(lst_item)
  }
  });
});
//$('ul.my_list').append('<li>Item</li>');