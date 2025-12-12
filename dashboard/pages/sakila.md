# Exploring Sakila Database

#Films in Sakilas

```sql films
select
    title,
    description,
    rating,
    length,
    release_year
from sakila.film;

```
## Top customer
```sql top_customers
SELECT * FROM rental_customer
```

<DataTable data={top_customers} />

<BarChart 
    data={top_customers}
    x=customer
    y=total_amount
    title="Top 10 Customers by Spending"
    swapXY=true
/>

## Films by Category
```sql films_by_category
SELECT * FROM categories
```

<DataTable data={films_by_category} />

<BarChart 
    data={films_by_category}
    x=category
    y=film_count
    title="Number of Films by Category"
    swapXY=true
/>