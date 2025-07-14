#!/usr/bin/node

const { argv } = require('node:process');
const input = parseInt(argv[2]);

if (isNaN(input)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${input}`);
}