-- tained in hbtn_0d_without a genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_show FULL OUTER JOIN tv_show_genres
ON tv_show.id = tv_show_genres.id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;