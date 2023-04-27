#!/usr/bin/node

const file = process.argv[2];
const srin = process.argv[3];
const fs = require('fs');
fs.writeFile(file, srin, 'utf8', (err) => { // fs.writeFile(file, data, options, callback)
  if (err) {
    console.error(err);
  }
});
