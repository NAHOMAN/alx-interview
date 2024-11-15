#!/usr/bin/node

const request = require('request');

// Read the Movie ID from the first argument
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Star Wars API URL for the given movie ID
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Fetch the movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Unable to fetch movie with ID ${movieId}`);
    return;
  }

  // Parse the response body
  const movie = JSON.parse(body);

  // Fetch and print each character's name
  const characters = movie.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }

      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
