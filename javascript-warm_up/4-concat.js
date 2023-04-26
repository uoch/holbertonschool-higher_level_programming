#!/usr/bin/node
const is = ' is ';
const args = process.argv;
if (args.length === 2) {
  console.log("undefined" + is + "undefined");
} else if (args.length === 3) {
  console.log(args[3] + is + "undefined");
} else {
  console.log(args[2] + is + args[4]);
}
