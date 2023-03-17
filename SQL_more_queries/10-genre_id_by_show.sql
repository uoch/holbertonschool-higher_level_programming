-- cript that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_shows.title , tv_show_genres.genre_id FROM tvshows
INNER JOIN tv_shows.title = tv_show_genres.genre_id
ORDER BY tv_shows.titlec ASC , tv_show_genres.genre_id  ASC;