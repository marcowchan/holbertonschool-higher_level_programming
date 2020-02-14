$.get('https://swapi.co/api/films/?format=json', function (data) {
  $('UL#list_movies').append(data.results.map(({ title }) => $(`<li>${title}</li>`)));
});
