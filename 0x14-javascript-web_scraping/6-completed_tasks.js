#!/usr/bin/node
const request = require('request');
request(process.argv[2], { json: true }, (err, response, body) => {
  if (err) {
    return console.log(err);
  }
  console.log(body.reduce((count, { userId, completed }) => {
    completed && (count[userId] ? count[userId]++ : count[userId] = 1);
    return count;
  }, {}));
});
