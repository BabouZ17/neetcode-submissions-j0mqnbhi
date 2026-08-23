-- Write your query below
select u.name, COALESCE(SUM(r.distance), 0) AS travelled_distance from users as u
LEFT JOIN rides AS r ON u.id = r.user_id
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, u.name ASC;