#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((prev, curr) => prev + (curr === searchElement ? 1 : 0), 0);
};
