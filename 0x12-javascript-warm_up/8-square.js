#!/usr/bin/node
// Prints the string 'Javascript is amazing'

function printSquare (number) {
  for (let i = 0; i < number; i++) {
    console.log(`${'X'.repeat(number)}`);
  }
}

const process = require('process');
parseInt(process.argv[2]) ? printSquare(parseInt(process.argv[2])) : console.log('Missing size');
