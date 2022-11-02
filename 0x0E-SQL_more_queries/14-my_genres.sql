-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name FROM tv_genres
INNER JOIN tv_show_genres g ON tv_genres.id = g.genre_id
INNER JOIN tv_show t ON g.show_id = t.id
WHERE t.title = 'Dexter'
ORDER BY tv_genres.name ASC;
