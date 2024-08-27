# Creating my database

## Steps
1. Open PgAdmin
2. Log Into Server
3. Create New Database: **Personal_Finance_Tracker**
4. Create New Table: **Test_Income_Table**
    - Create Columns: **id, source, amount, date**

5. Repeat Step 4 for **Expenses and Savings Goals**


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

```
INSERT INTO public."Test_Savings_Goals_Table"(
	"Goal", "Goal Type", "Goal Amount", "Start Date", "End Date")
VALUES (?, ?, ?, ?, ?);
```
