#!/usr/bin/node
const a = process.argv;
const z = 0;
a.sort(function (a, b) {
  return b - a; // ascending order
});
if (a.length === 2) {
  console.log(z);
} else if (a.length === 3) {
  if (parseInt(a[2])) {
    console.log(z);
  } else {
    console.log(a[2]);
  }
} else {
  console.log(a[3]);
}
