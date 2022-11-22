#### Functional Programming.


### PART A
In Part A, the goal is to build a program to report the transactions for a particular stock in a human-
readable format. For example, for our test data set, the transactions on the stock VTI will be printed
as:
--- Bought 100 units of VTI for 1104 pounds each on day 1
--- Bought 50 units of VTI for 1223 pounds each on day 5
--- Sold 150 units of VTI for 1240 pounds each on day 9

###### Question 1
```{python}

single_transaction = ("B", 100,1104,"VTI",1)
transaction_to_string(single_transaction)
```

###### Question 2

```{python}
sample_transactions = [
        ("B", 100,1104,"VTI",1),
        ("B", 200,36,"ONEQ",3),
        ("B", 50, 1223, "VTI", 5),
        ("S", 150,1240,"VTI",9),
        ("B", 100, 229, "IWRD", 10),
        ("S", 200, 32, "ONEQ", 11),
        ("S", 100, 210, "IWRD",12)
]

trade_report_list(sample_transactions[:3])

```
###### Question 2
This function takes a list of transactions, and converts each transaction into a string
```{python}
sample_transactions = [
        ("B", 100,1104,"VTI",1),
        ("B", 200,36,"ONEQ",3),
        ("B", 50, 1223, "VTI", 5),
        ("S", 150,1240,"VTI",9),
        ("B", 100, 229, "IWRD", 10),
        ("S", 200, 32, "ONEQ", 11),
        ("S", 100, 210, "IWRD",12)
]



```
###### Question 3
This function takes a stock and a transaction log, and returns True if the transaction trades that stock, and False otherwise.
```{python}
stock_test("VTI",  ("B", 100,1104,"VTI",1))

```

###### Question 4
This function takes a stock and a transaction log, and returns all trades in the transaction log that trade the given
stock
```{python}

sample_transactions = [
        ("B", 100,1104,"VTI",1),
        ("B", 200,36,"ONEQ",3),
        ("B", 50, 1223, "VTI", 5),
        ("S", 150,1240,"VTI",9),
        ("B", 100, 229, "IWRD", 10),
        ("S", 200, 32, "ONEQ", 11),
        ("S", 100, 210, "IWRD",12)
]


get_trades("VTI", sample_transactions)
```
###### Question 5 Trade Report

This function takes a stock and a transaction log, and returns a string containing the human-readable version of the log
```{python}

sample_transactions = [
        ("B", 100,1104,"VTI",1),
        ("B", 200,36,"ONEQ",3),
        ("B", 50, 1223, "VTI", 5),
        ("S", 150,1240,"VTI",9),
        ("B", 100, 229, "IWRD", 10),
        ("S", 200, 32, "ONEQ", 11),
        ("S", 100, 210, "IWRD",12)
]


trade_report("VTI", sample_transactions)
```


#### PART B
In Part B, the goal is to build a function to tell the user how much profit or loss was made on each stock.
For our test data set, this report will be:
-- VTI: 14450
-- ONEQ: -800
--- IWRD: -1900


###### Question 6
The function takes a transaction and the current amount of money that you have, and returns the amount of money that you have
after the transaction
```{python}
update_money(("B", 100,1104,"VTI",1) 100)
```

###### Question 7
The function takes a transaction log and the name of a stock, and returns the total amount of profit or loss made for that stock.

```{python}
sample_transactions = [
        ("B", 100,1104,"VTI",1),
        ("B", 200,36,"ONEQ",3),
        ("B", 50, 1223, "VTI", 5),
        ("S", 150,1240,"VTI",9),
        ("B", 100, 229, "IWRD", 10),
        ("S", 200, 32, "ONEQ", 11),
        ("S", 100, 210, "IWRD",12)
]


profit("VTI", sample_transactions)
```


###### Question 8
The function takes a list of stocks and a transaction log, and returns the human-readable string containing the profit and
loss report

```{python}
sample_transactions = [
        ("B", 100,1104,"VTI",1),
        ("B", 200,36,"ONEQ",3),
        ("B", 50, 1223, "VTI", 5),
        ("S", 150,1240,"VTI",9),
        ("B", 100, 229, "IWRD", 10),
        ("S", 200, 32, "ONEQ", 11),
        ("S", 100, 210, "IWRD",12)
]


profit_report(["VTI", "ONEQ"], sample_transactions)
```

#### PART C

###### Question 9
This function takes a transaction log and a price database, and returns a profit and loss report in the same format
```{python}
price_database = [
        ("VTI", [1689, 1785, 1772, 1765, 1739, 1725, 1615, 1683, 1655, 1725, 1703, 1726, 1725,
            1742, 1707, 1688, 1697, 1688, 1675]),
        ("ONEQ", [201, 203, 199, 199, 193, 189, 189, 183, 185, 190, 186, 182, 186, 182, 182,
            186, 183, 179, 178]),
        ("IWRD", [207, 211, 213, 221, 221, 222, 221, 218, 226, 234, 229, 229, 228, 222, 218,
            223, 222, 218, 214])
]


complex_profit_report(stock, price_database)
```
