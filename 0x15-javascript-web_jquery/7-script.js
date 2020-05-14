// Javascript script that fetches and replaces the name
// Must use the jQuery API

$.getJSON('https://swapi.co/api/people/5/?format=json', function (data) {
    $('DIV#character').html(data['name']);
});
