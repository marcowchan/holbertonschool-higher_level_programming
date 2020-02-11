#!/usr/bin/node
const request = require('request');
const count = {};
request(process.argv[2], { json: true }, (err, response, body) => {
  if (err) {
    return console.log(err);
  }
  body.forEach(({ userId, completed }) => {
    count[userId] = count[userId] || 0;
    count[userId] += completed ? 1 : 0;
  });
  console.log(count);
});
