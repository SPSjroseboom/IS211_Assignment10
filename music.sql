CREATE TABLE artist (
artist_name TEXT PRIMARY KEY
);

CREATE TABLE albums (
id INTEGER PRIMARY KEY,
artist_name TEXT,
album_name TEXT
);

CREATE TABLE songs (
id INTEGER PRIMARY KEY,
album_name TEXT,
song_name TEXT,
track_number INTEGER,
song_length INTEGER
);