#!/usr/bin/node
exports.esrever = function (list) {
  return list.map((ele, i) => list[list.length - i - 1]);
};
