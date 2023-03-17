-- Import the database dump from hbtn_0d_tvshows to your MySQL server:
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_show LEFT JOIN tv_show_genres
ON tv_show.id = tv_show_genres.id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;