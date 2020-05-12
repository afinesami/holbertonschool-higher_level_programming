#!/usr/bin/node
// prints the number of movies where the character Wedge Antilles is present

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const list = (JSON.parse(body).results);
    let cont_characters = 0;
    for (let cont = 0; cont < list.length; cont++) {
      for (let cont1 = 0; cont1 < list[cont1].characters.length; cont1++) {
        if (list[cont1].characters.includes('https://swapi-api.hbtn.io/api/films/')) {
          cont_characters++;
        }
      }
    }
      console.log(cont_characters);
  }
});
