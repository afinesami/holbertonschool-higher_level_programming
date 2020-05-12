#!/usr/bin/node
// script that prints the title of a Star Wars movie

const args = process.argv;
let reqURL = 'http://swapi.co/api/films/' + args[2] + '/';
let request = require('request');
request(reqURL, function (error, response, body) {
// Print the error if one occurred
  if (error) {
    console.log('error:', error);
  } else {
    let jso = JSON.parse(body);
    console.log(jso['title']);
  }
});
