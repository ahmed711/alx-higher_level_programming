#!/usr/bin/node
// Prints the string 'Javascript is amazing'

const process = require('process');

if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
