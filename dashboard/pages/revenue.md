# Revenue Analysis

Analysis of revenue in Sakila DVD rental.

## Total Revenue
```sql total_revenue
SELECT 
    ROUND(SUM(amount), 2) as total_revenue,
    COUNT(*) as total_transactions
FROM payment
```

<BigValue 
    data={total_revenue}
    value=total_revenue
    title="Total Revenue"
    fmt="$#,##0.00"
/>

<BigValue 
    data={total_revenue}
    value=total_transactions
    title="Total Transactions"
/>

---

## Top 10 Customers by Revenue
```sql revenue_by_customer
SELECT * FROM rental_customer
```

<BarChart 
    data={revenue_by_customer}
    x=customer
    y=total_amount
    title="Revenue by Customer"
    swapXY=true
/>

---

## Recent Payments
```sql recent_payments
SELECT 
    payment_id,
    customer_id,
    amount,
    payment_date
FROM payment
ORDER BY payment_id DESC
LIMIT 20
```

<DataTable data={recent_payments} />