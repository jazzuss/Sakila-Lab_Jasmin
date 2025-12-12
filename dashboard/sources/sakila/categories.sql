SELECT 
    c.name as category,
    COUNT(fc.film_id) as film_count
FROM category c
LEFT JOIN film_category fc ON c.category_id = fc.category_id
GROUP BY c.name
ORDER BY film_count DESC