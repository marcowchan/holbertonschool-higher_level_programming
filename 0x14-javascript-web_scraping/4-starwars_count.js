#!/usr/bin/node
const request = require('request');
const wedge = 'https://swapi.co/api/people/18/';
request(process.argv[2], { json: true }, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  console.log(body.results.reduce((prev, curr) => curr.characters.includes(wedge) ? 1 + prev : prev, 0));
});
