#!/usr/bin/node
const request = require('request');
request(`http://swapi.co/api/films/${process.argv[2]}`, { json: true }, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  console.log(body.title);
});
