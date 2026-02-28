-- Lists all genres not linked to the show Dexter.
-- The tv_shows table contains only one record where title = Dexter.
-- Results are sorted in ascending order by the genre name.
-- Uses a subquery to find Dexter's genres and excludes them from the main list.

SELECT name
  FROM tv_genres
 WHERE name NOT IN (
      SELECT g.name
        FROM tv_genres AS g
             INNER JOIN tv_show_genres AS s_g
             ON g.id = s_g.genre_id

             INNER JOIN tv_shows AS s
             ON s_g.show_id = s.id
       WHERE s.title = 'Dexter'
 )
 ORDER BY name ASC;
