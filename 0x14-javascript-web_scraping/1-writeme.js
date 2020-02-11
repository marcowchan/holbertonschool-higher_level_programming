#!/usr/bin/node
const { writeFile } = require('fs');
writeFile(process.argv[2], process.argv[3], 'utf8', (err) => {
  if (err) {
    return console.log(err);
  }
});
