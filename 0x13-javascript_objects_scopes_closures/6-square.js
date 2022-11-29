#!/usr/bin/node
const oSquare = require('./5-square');

class Square extends oSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let n = 0; n < this.height; n++) {
      let s = '';
      for (let m = 0; m < this.width; m++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
