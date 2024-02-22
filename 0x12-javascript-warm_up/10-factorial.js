#!/usr/bin/node
// Prints the string 'Javascript is amazing'

function factorial (number) {
  if (number === 1) {
    return number;
  } else {
    return number * factorial(number - 1);
  }
}

const process = require('process');
parseInt(process.argv[2]) ? console.log(factorial(parseInt(process.argv[2]))) : console.log(1);
