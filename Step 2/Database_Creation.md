# Creating my database

## Steps
1. Open PgAdmin
2. Log Into Server
3. Create New Database: **Test_Income_Table**
4. Create New Table: **Test Table**
    - Create Columns: **id, source, amount, date**

## Table Queries Used
```
INSERT INTO public."Test_Income_Table"(
	"Name", "Source", "Amount", "Date")
VALUES ('Unemployment', 'Unemployment', 288.88, '08/27/2024')
```

```
SELECT "Name", "Source", "Amount", "Date"
FROM public."Test_Income_Table";
```