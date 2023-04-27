#!/usr/bin/node
function converter (base) {
  return function (n) {
    return n.toString(base);
  };
}
exports.converter = converter;
