DROP TABLE IF EXISTS flashcards;

CREATE TABLE flashcards (
  id SERIAL PRIMARY KEY,
  question VARCHAR(255),
  answer VARCHAR(255)
);

