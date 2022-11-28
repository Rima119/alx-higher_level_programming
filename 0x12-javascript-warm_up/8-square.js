#!/usr/bin/node

let n = process.argv[2];

if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    let s = '';
    for (let j = 0; j < n; j++) {
      s = s + 'X';
    }
    console.log(s);
  }
}
