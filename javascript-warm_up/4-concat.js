#!/usr/bin/node
const is = ' is ';
const sp = ' '
const args = process.argv;
if (args.length === 1) {
  console.log(args.length);
  console.log("undefined" + is + "undefined");
} else if (args.length === 4) {
  console.log(args.length);
  console.log(args[2] + sp+ args[3]);
} else {
  console.log(args.length);
  console.log(args[2] + is + args[4]);
}
