#!/usr/bin/node
// Prints the string 'Javascript is amazing'

function printMultiple (number) {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}

const process = require('process');
parseInt(process.argv[2]) ? printMultiple(parseInt(process.argv[2])) : console.log('Missing number of occurrences');
