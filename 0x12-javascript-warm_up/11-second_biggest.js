#!/usr/bin/node
if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log(0);
} else {
  console.log(process.argv.slice(2).map(e => parseInt(e)).sort((a, b) => b - a)[1]);
}
