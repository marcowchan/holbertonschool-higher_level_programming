#!/usr/bin/node
const dict = require('./main').dict;
const inverted = {};
for (const key in dict) {
  if (inverted[dict[key]] === undefined) {
    inverted[dict[key]] = [];
  }
  inverted[dict[key]].push(key);
}
console.log(inverted);
