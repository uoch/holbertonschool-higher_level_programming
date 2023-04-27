#!/usr/bin/node
function serch (a) {
  const nn = 'https://swapi-api.hbtn.io/api/people/18/';
  for (let i = 0; i < a.length; i++) {
    if (a[i] === nn) {
      return (i);
    }
  }
}

const request = require('request');
const n = process.argv[2];
if (!n) {
  console.error('Usage: node 4-starwars_count.js <url>');
  process.exit(1);
}
const url = n;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const h = serch(movie.results[0].characters);
    request(movie.results[0].characters[h], (error, response, body) => {
      if (error) {
        console.error(error);
      } else {
        const actor = JSON.parse(body);
        if (h === 0) {
          console.log(h);
        } else {
          console.log(actor.films.length);
        }
      }
    });
  }
});
