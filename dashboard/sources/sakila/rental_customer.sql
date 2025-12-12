SELECT 
    c.first_name || ' ' || c.last_name as customer,
    COUNT(r.rental_id) as number_of_rentals,
    ROUND(SUM(p.amount), 2) as total_amount
FROM customer c
LEFT JOIN rental r ON c.customer_id = r.customer_id
LEFT JOIN payment p ON c.customer_id = p.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_amount DESC
LIMIT 10