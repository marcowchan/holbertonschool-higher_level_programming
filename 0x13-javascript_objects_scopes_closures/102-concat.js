#!/usr/bin/node
const { readFile, writeFile } = require('fs');
readFile(process.argv[2], 'utf8', (err, dataA) => {
  if (err) throw err;
  readFile(process.argv[3], 'utf8', (err, dataB) => {
    if (err) throw err;
    writeFile(process.argv[4], dataA + dataB, 'utf8', (err) => {
      if (err) throw err;
    });
  });
});
