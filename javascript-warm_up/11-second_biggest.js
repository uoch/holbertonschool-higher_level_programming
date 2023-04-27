#!/usr/bin/node
const a = process.argv;
let z = 0;
  a.sort(function(a, b) {
    return b - a; // ascending order
  });
if(a.length===2){
  console.log(z);
}else if(a.length ===3){
  console.log(a[2]);
}else{
  console.log(a[3]);
}
