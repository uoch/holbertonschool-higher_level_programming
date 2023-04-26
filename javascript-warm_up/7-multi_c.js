#!/usr/bin/node
const args = process.argv;
const line = 'C is fun';
const numTimes = parseInt(args[2]);
if (numTimes === undefined) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < numTimes; i++) {
  console.log(line);
}
