#!/usr/bin/node
const movie = process.argv[2];
const request = require('request');

request(movie, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const tasksCompleted = data.reduce((acc, task) => {
      if (task.completed) {
        if (acc[task.userId]) {
          acc[task.userId]++;
        } else {
          acc[task.userId] = 1;
        }
      }
      return acc;
    }, {});

    console.log(tasksCompleted);
  }
});
