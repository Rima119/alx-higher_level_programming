#!/usr/bin/node

let n = process.argv[2];

if (!isNaN(parseInt(n))) {
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
} else {
console.log('Missing number of occurrences');
}
