#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
request('https://swapi-api.hbtn.io/api/films/' + id, function title (error, response, body) {
  if (error) {
    console.error(error);
  }
  const parsed = JSON.parse(body);
  console.log(parsed.title);
});