#!/usr/bin/node
const { argv } = require('node:process');

function add (a, b) {
  return a + b;
}

const a = parseInt(argv[2]);
const b = parseInt(argv[3]);
console.log(add(a, b));
