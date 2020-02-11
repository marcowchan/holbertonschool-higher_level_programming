#!/usr/bin/node
const dict = require('./101-data').dict;
let inverted = {};
for (key in dict) {
  if (inverted[dict[key]] === undefined) {
    inverted[dict[key]] = [];
  }
  inverted[dict[key]].push(key);
}
console.log(inverted);
