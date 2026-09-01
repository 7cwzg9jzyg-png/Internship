# Budget App

A Python project to track spending across different budget categories and visualize spending patterns through bar charts.

## Overview

This project implements a `Category` class to manage budget tracking and a `create_spend_chart` function to visualize spending distribution across categories.

## Features

### Category Class

The `Category` class represents a budget category (e.g., Food, Clothing, Entertainment).

**Constructor:**
```python
category = Category("Food")
```

**Attributes:**
- `name`: The name of the category
- `ledger`: A list of transactions, each stored as `{"amount": amount, "description": description}`

**Methods:**

#### `deposit(amount, description="")`
Add money to the category.
```python
food.deposit(1000, "salary")
food.deposit(50)  # Description defaults to empty string
```

#### `withdraw(amount, description="")`
Remove money from the category if sufficient funds exist.
- Returns `True` if withdrawal was successful, `False` otherwise
```python
success = food.withdraw(10.15, "groceries")
```

#### `get_balance()`
Return the current balance of the category.
```python
balance = food.get_balance()  # Returns sum of all transactions
```

#### `transfer(amount, other_category)`
Transfer money to another category.
- Creates a withdrawal from this category with description "Transfer to [Category Name]"
- Creates a deposit in the other category with description "Transfer from [Category Name]"
- Returns `True` if transfer was successful, `False` if insufficient funds
```python
food.transfer(50, clothing)  # Transfers $50 from food to clothing
```

#### `check_funds(amount)`
Check if sufficient funds exist for a transaction.
- Returns `True` if balance >= amount, `False` otherwise
```python
can_afford = food.check_funds(100)
```

#### `__str__()`
Return a formatted string representation showing:
1. Category name centered in a 30-character line of asterisks
2. Ledger items with description (first 23 chars) and amount (right-aligned, 7 chars, 2 decimals)
3. Total balance
```python
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food)
```

Output:
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Total: 974.96
```

### create_spend_chart Function

Generate a bar chart showing percentage of total spending for each category.

**Parameters:**
- `categories`: A list of Category objects

**Returns:**
- A string containing a formatted bar chart

**Features:**
- Calculates percentage spent (only withdrawals count, not deposits)
- Each bar is built from 'o' characters
- Heights are rounded down to nearest 10%
- Y-axis shows percentages from 0-100
- X-axis shows category names written vertically

**Example:**
```python
food = Category("Food")
food.deposit(1000)
food.withdraw(50)

clothing = Category("Clothing")
clothing.deposit(1000)
clothing.withdraw(25)

auto = Category("Auto")
auto.deposit(1000)
auto.withdraw(25)

chart = create_spend_chart([food, clothing, auto])
print(chart)
```

**Output:**
```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    -----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

## Example Usage

```python
from main import Category, create_spend_chart

# Create categories
food = Category("Food")
clothing = Category("Clothing")

# Add transactions
food.deposit(1000, "salary")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant")
food.transfer(50, clothing)

clothing.deposit(50, "from food transfer")
clothing.withdraw(25.55, "shirts")

# Print category details
print(food)
print(clothing)

# Generate spending chart
chart = create_spend_chart([food, clothing])
print(chart)
```

## Implementation Notes

- Withdrawals are stored as negative amounts in the ledger
- Transfers create entries in both categories showing the source/destination
- Check_funds is used internally by withdraw and transfer methods
- The spend chart calculation only considers withdrawals (negative amounts)
- All line lengths in the chart are consistent and exactly match expected formatting
- Chart can handle 1-4 categories

## Running the Demo

```bash
python demo.py
```

## Running Tests

```bash
python -m unittest test_main -v
```
