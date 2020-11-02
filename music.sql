DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS songs;

CREATE TABLE artists (
	artist_id INTEGER PRIMARY KEY,
	first_name TEXT,
	last_name TEXT
);

CREATE TABLE albums (
	album_id INTEGER PRIMARY KEY,
	artist_id INTEGER,
	album_title TEXT,
	FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);

CREATE TABLE songs (
	song_id INTEGER PRIMARY KEY,
	album_id INTEGER,
	song_track_num INTEGER,
	song_length INTEGER,
	FOREIGN KEY(album_id) REFERENCES album(album_id)
);
