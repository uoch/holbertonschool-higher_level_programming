#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !w || !h) {
      // undifined
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const line = 'X';
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

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
