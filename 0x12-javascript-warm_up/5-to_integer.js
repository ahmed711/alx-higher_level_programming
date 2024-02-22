#!/usr/bin/node
// Prints the string 'Javascript is amazing'

const process = require('process');
const myVar = parseInt(process.argv[2]) ? `My number: ${parseInt(process.argv[2])}` : 'Not a number';

console.log(myVar);
