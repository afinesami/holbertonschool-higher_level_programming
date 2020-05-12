#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');
const file = process.argv[3];
const url = process.argv[2];
const write_ = request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body));
  }
});

fs.writeFile(file, write_, 'utf8', function (error) {
  if (error) {
    console.log(error);
  }
});
