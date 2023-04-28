const ur = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$(() => {
  $.getJSON(ur, (data) => {
    $('#character').text(data.name);
  });
});
