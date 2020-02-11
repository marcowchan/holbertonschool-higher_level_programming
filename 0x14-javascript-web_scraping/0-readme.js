#!/usr/bin/node
const { readFile } = require('fs');
readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
