create table Genre (
    id serial primary key,
    name varchar(200) not null unique
);

create table Performer (
	id serial primary key,
	name varchar(200) not null unique,
	genre_id integer references Genre(id)
);

create table Albums (
	id serial primary key,
	performer_id integer references Performer(id),
	name varchar(200) not null,
	release date
);

create table Track (
	id serial primary key,
	albums_id integer references Albums(id),
	duration numeric,
	name varchar(200) not null
);