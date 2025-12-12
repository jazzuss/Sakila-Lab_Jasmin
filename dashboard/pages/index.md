# Sakila DVD Rental - Dashboard

Welcome to the Sakila Dashboard.

## Quick Stats
```sql quick_stats
SELECT 
    (SELECT COUNT(*) FROM film) as total_films,
    (SELECT COUNT(*) FROM customer) as total_customers,
    (SELECT COUNT(*) FROM rental) as total_rentals,
    (SELECT ROUND(SUM(amount), 2) FROM payment) as total_revenue
```

<BigValue 
    data={quick_stats}
    value=total_films
    title="Total Films"
/>

<BigValue 
    data={quick_stats}
    value=total_customers
    title="Total Customers"
/>

<BigValue 
    data={quick_stats}
    value=total_rentals
    title="Total Rentals"
/>

<BigValue 
    data={quick_stats}
    value=total_revenue
    title="Total Revenue"
    fmt="$#,##0.00"
/>

---

## Top Customers
```sql top_5_customers
SELECT * FROM rental_customer LIMIT 5
```

<BarChart 
    data={top_5_customers}
    x=customer
    y=total_amount
    title="Top 5 Customers by Spending"
/>

---

## Films by Category
```sql category_overview
SELECT * FROM categories LIMIT 8
```

<BarChart 
    data={category_overview}
    x=category
    y=film_count
    title="Films by Category"
/>

---

## Navigation

- [Films](/films) - Detailed film analysis
- [Customers](/customers) - Customer insights  
- [Revenue](/revenue) - Revenue analysis
- [Sakila](/sakila) - Complete overview