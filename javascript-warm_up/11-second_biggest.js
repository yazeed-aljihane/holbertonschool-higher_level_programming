#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length < 4) {
  console.log(0);
  process.exit(0);
}
let biggest = 0;
let secondBiggest = 0;
for (let i = 2; i < argv.length; i++) {
  argv[i] = parseInt(argv[i]);
  if (isNaN(argv[i])) {
    continue;
  }
  if (argv[i] > biggest) {
    secondBiggest = biggest;
    biggest = argv[i];
  } else if (argv[i] > secondBiggest && argv[i] !== biggest) {
    secondBiggest = argv[i];
  }
}
console.log(secondBiggest);
