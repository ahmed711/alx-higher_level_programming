#!/usr/bin/node
// Prints the string 'Javascript is amazing'

const process = require('process');

process.argv[2] ? console.log(process.argv[2]) : console.log('No argument');
