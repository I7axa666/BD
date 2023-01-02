CREATE TABLE IF NOT EXISTS Geners(
	id SERIAL PRIMARY KEY,
	gener_name VARCHAR(40) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Performers (
	id SERIAL PRIMARY KEY,
	performer_name VARCHAR(40)UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS GenerPerformer (
	gener_id INTEGER REFERENCES Geners(id),
	performer_id INTEGER REFERENCES Performers(id),
	CONSTRAINT pk PRIMARY KEY (gener_id, performer_id)
);

CREATE TABLE IF NOT EXISTS Albums (
	id SERIAL PRIMARY KEY,
	album_name VARCHAR(40) UNIQUE NOT NULL,
	album_year INTEGER CHECK (album_year >= 1900)
);

CREATE TABLE IF NOT EXISTS PerfoprmerAlbums (
	id SERIAL PRIMARY KEY,
	performer_id INTEGER REFERENCES Performers(id),
	albums_id INTEGER REFERENCES Albums(id)
);

CREATE TABLE IF NOT EXISTS Tracks (
	id SERIAL PRIMARY KEY,
	track_name VARCHAR(40),
	duration INTEGER CHECK (duration > 0 AND duration < 1000),
	abums_id INTEGER REFERENCES Albums(id)
);

CREATE TABLE IF NOT EXISTS Collections (
	id SERIAL PRIMARY KEY,
	coll_name VARCHAR(40),
	coll_year INTEGER CHECK (coll_year > 1900)
);

CREATE TABLE IF NOT EXISTS TrackCollection (
	id SERIAL PRIMARY KEY,
	track_id INTEGER REFERENCES Tracks(id),
	collection_id INTEGER REFERENCES Collections(id)
	
);