-- script que enumera todos los programas contenidos en HBTN_0D_TVShows que tienen al menos un género vinculado.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;