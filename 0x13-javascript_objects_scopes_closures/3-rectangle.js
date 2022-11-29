#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let n = 0; n < this.height; n++) {
      let r = '';
      for (let m = 0; m < this.width; m++) {
        r += 'X';
      }
      console.log(r);
    }
  }
}

module.exports = Rectangle;
