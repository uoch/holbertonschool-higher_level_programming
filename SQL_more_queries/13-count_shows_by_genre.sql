-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name AS genre , COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres
GROUP BY   genre
ORDER BY number_of_shows DESC;