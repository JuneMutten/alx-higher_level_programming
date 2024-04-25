#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf-8', (error, data) => {
  if (error) {
    console.error('Error reading file:', error);
    return;
  }
  console.log(data);
});