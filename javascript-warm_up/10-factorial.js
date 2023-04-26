#!/usr/bin/node
function fact (a) {
  const aa = parseInt(a);
  if (aa < 0) {
    return 'Input must be a non-negative integer';
  }
  if (aa === 0 || isNaN(aa)) {
    return 1;
  }
  return (aa * fact(aa - 1));
}
const arg1 = process.argv[2];
console.log(fact(arg1));
