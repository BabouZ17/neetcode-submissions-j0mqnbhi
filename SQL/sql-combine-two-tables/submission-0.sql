SELECT p.first_name, p.last_name, a.city, a.state 
FROM person as p 
LEFT JOIN address as a ON p.person_id = a.person_id