-- Lists all comedy shows.
-- Lists all comedy shows.
SELECT tv_shows.title
	FROM tv_genres, tv_show_genres, tv_shows
	WHERE tv_genres.name = "Comedy"
	AND tv_show_genres.show_id = tv_shows.id
	AND tv_show_genres.genre_id = tv_genres.id
	ORDER BY title;
