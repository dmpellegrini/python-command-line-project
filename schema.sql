DROP TABLE IF EXISTS flashcards;

CREATE TABLE authors (
  id SERIAL PRIMARY KEY,
  question VARCHAR(255),
  answer VARCHAR(255),
);

