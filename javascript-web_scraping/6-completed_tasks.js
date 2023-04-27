#!/usr/bin/node
const movie = process.argv[2];
const file = process.argv[3];
const request = require('request');
let teskComplite = 0;

request(movie, (error, response, body) => {
    if (error) {
        console.error(error);
    } else {
        let data = JSON.parse(body);
        let tasksCompleted = data.reduce((acc, task) => {
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
