#!/usr/bin/node
const request = require('request');
const wedge = '18';
request(process.argv[2], { json: true }, (err, response, body) => {
  if (err) {
    return console.log(err);
  }
  console.log(body.results.reduce((prev, curr) => {
    curr.characters.forEach(char => char.includes(wedge) && prev++);
    return prev;
  }, 0));
});
