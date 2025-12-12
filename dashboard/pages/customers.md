# Customer Analysis

Analysis of customers in the Sakila DVD rental database.

## Top 10 Customers by Spending
```sql top_customers
SELECT * FROM rental_customer
```

<DataTable data={top_customers} />

<BarChart 
    data={top_customers}
    x=customer
    y=total_amount
    title="Top 10 Customers by Total Spending"
    swapXY=true
/>

---

## All Customers
```sql all_customers
SELECT 
    customer_id,
    first_name,
    last_name,
    email,
    active
FROM customer
LIMIT 50
```

<DataTable data={all_customers} search=true />