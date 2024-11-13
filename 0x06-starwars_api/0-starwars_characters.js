#!/usr/bin/node

const request = require('request');

<<<<<<< HEAD
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});
const exactOrder = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(actors, x + 1);
  });
};
=======
const movieId = process.argv[2];
const filmEndPoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let people = [];
const names = [];

const requestCharacters = async () => {
  await new Promise(resolve => request(filmEndPoint, (err, res, body) => {
    if (err || res.statusCode !== 200) {
      console.error('Error: ', err, '| StatusCode: ', res.statusCode);
    } else {
      const jsonBody = JSON.parse(body);
      people = jsonBody.characters;
      resolve();
    }
  }));
};

const requestNames = async () => {
  if (people.length > 0) {
    for (const p of people) {
      await new Promise(resolve => request(p, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          console.error('Error: ', err, '| StatusCode: ', res.statusCode);
        } else {
          const jsonBody = JSON.parse(body);
          names.push(jsonBody.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: Got no Characters for some reason');
  }
};

const getCharNames = async () => {
  await requestCharacters();
  await requestNames();

  for (const n of names) {
    if (n === names[names.length - 1]) {
      process.stdout.write(n);
    } else {
      process.stdout.write(n + '\n');
    }
  }
};

getCharNames();
>>>>>>> b03a39528f712dd0ea29286a3055f7a736b28e28
