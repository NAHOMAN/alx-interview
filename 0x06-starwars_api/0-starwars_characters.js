#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Get the Movie ID from the command-line argument
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// URL for the Star Wars API films endpoint
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make a request to get the movie details
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

  // Get the list of character URLs
  const characters = movie.characters;

  // Fetch and print each character's name
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
