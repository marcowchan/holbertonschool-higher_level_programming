#!/usr/bin/node
function fact (a) {
  if (isNaN(a) || a === 1 || a === 0) {
    return 1;
  }
  return a * fact(a - 1);
}
console.log(fact(parseInt(process.argv[2])));
