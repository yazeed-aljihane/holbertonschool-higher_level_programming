#!/usr/bin/node
const { argv } = require('node:process');
const num = parseInt(argv[2]);
if (isNaN(num)) {
  console.log(1);
} else {
  const factorial = (n) => {
    if (n === 0 || n === 1) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  };
  console.log(factorial(num));
}
