#!/usr/bin/node
const is = ' is ';
const args = process.argv;
if (args.length === 1) {
  console.log("undefined" + is + "undefined");
} else if (args.length === 3) {
  console.log(args[2] + args[3]);
} else {
  console.log(args[2] + is + args[4]);
}
