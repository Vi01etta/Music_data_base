
create table Genre (
	id serial primary key,
	name varchar(200) not null unique
);

create table Performer (
	id serial primary key,
	name varchar(200) not null unique
);

create table GenrePerformer (
	genre_id integer references Genre(id),
	performer_id integer references Performer(id)
);

create table Albums (
	id serial primary key,
	name varchar(200) not null,
	release integer
);

create table PerformerAlbums (
	Album_id integer references Albums(id),
	performer_id integer references Performer(id)
);

create table Track (
	id serial primary key,
	albums_id integer references Albums(id),
	duration numeric,
	name varchar(200) not null
);

create table Collections (
	id serial primary key,
	name varchar(200) not null,
	release integer
);

create table CollectionsTrack (
        Collections_id integer references Collections(id),
	Track_id integer references Track(id)
);
