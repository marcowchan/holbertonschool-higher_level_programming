#!/usr/bin/node
const request = require('request');
const names = [];
let len = 0;
request(`http://swapi.co/api/films/${process.argv[2]}`, { json: true }, (err, response, films) => {
  if (err) {
    return console.log(err);
  }
  films.characters.forEach((url, i) => {
    request(url, { json: true }, (err, response, char) => {
      if (err) {
        return console.log(err);
      }
      names[i] = char.name;
      len++;
      if (len === films.characters.length) {
        names.forEach(name => console.log(name));
      }
    });
  });
});
