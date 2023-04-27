#!/usr/bin/node
function nbOccurences (list, searchElement) {
  let k = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      k += 1;
    }
  }
  return k;
}

exports.nbOccurences = nbOccurences;
