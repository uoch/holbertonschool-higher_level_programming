#!/usr/bin/node
const Rectangle = require('./5-square');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      const line = c;
      let row = '';
      const ss = '\n';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          row += line;
        }
        if (i === (this.height - 1)) {
          break;
        }
        row += ss;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
