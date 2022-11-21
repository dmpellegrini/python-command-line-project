# Vim Flash Cards

Welcome to Vim Flashcards.  The command line app specializing in memorizing Vim stuff.

## Dependencies

To use this app you will need to have the following dependencies installed

- python3
- pipenv
- postgresql

## Setup

There is a bit of setup involved in order to run the app as it depends on a postgres database and a pipenv virtual environment

- Fork and clone down this repository, then navigate to the home directory 

- Once you have installed postgres enter the following command into your terminal shell

```
createdb flashcards
```

- Alternatively enter the following command while in postgres

```
CREATE DATABASE flashcards;
```

- This will set up the flashcards database

- After this step, run the following commands from the command line

```
$ psql -d flashcards < schema.sql
$ psql -d flashcards < seed.sql
```

- This will seed the database with a flashcards table

- Finally, set up the virtual environment by running the following command 

```
pipenv shell
```

## Usage

Once everything is set up, run the following command to run the app

```
python3 app.py
```

You will be greeted with a message welcoming you to the Vim Flashcards App and you can proceed from there
