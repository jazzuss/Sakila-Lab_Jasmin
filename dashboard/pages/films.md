# Film Analysis

Analysis of films in the Sakila DVD library.

## All Films
```sql all_films
SELECT * FROM film
```

<DataTable data={all_films} search=true />

---

## Films by Rating
```sql films_by_rating
SELECT 
    rating,
    COUNT(*) as film_count
FROM film
GROUP BY rating
ORDER BY film_count DESC
```

<DataTable data={films_by_rating} />

<BarChart 
    data={films_by_rating}
    x=rating
    y=film_count
    title="Distribution of Films by Rating"
/>

---

## Films by Category
```sql films_by_category
SELECT * FROM categories
```

<BarChart 
    data={films_by_category}
    x=category
    y=film_count
    title="Number of Films by Category"
    swapXY=true
/>