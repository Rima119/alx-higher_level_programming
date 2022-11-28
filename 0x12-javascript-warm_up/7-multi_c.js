#!/usr/bin/node

let n = process.argv[2];

if (n) {
  let m = 0;
  n = parseInt(n);
  while (m < n) {
    console.log('C is fun');
    m++;
  }
} else {
  console.log('Missing number of occurrences');
}
