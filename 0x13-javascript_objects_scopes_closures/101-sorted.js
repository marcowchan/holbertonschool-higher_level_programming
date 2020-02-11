#!/usr/bin/node
const dict = require('./101-data').dict;
const inverted = {};
for (const key in dict) {
  if (inverted[dict[key]] === undefined) {
    inverted[dict[key]] = [];
  }
  inverted[dict[key]].push(key);
}
console.log(inverted);
