#!/usr/bin/node
const args = process.argv;
const line = 'X';
let row = ''
const ss = '\n'
const numTimes = parseInt(args[2]);
if (numTimes === undefined) {
  console.log('Missing size');
}
for (let i = 0; i < numTimes; i++) {
  for (let j = 0; j < numTimes; j++) {
    row += line;
  }
  if (i === (numTimes - 1)) {
    break;
  }
  row += ss
}
console.log(row);
