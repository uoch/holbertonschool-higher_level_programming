#!/usr/bin/node

const request = require('request');
const n = process.argv[2];

const url = n;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    request(movie.results[0].characters[15], (error, response, body) => {
      if (error) {
        console.error(error);
      } else {
        const actor = JSON.parse(body);
        console.log(actor.films.length);
      }
    });
  }
});
