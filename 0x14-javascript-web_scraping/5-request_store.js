#!/usr/bin/node
const request = require('request');
const { writeFile } = require('fs');
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  }
  writeFile(process.argv[3], body, 'utf8', (err) => {
    if (err) {
      return console.log(err);
    }
  });
});
