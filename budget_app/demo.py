from main import Category, create_spend_chart


# Create budget categories
food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

# Test deposit and withdraw
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
food.transfer(50, clothing)

clothing.deposit(50, "from food transfer")
clothing.withdraw(25.55, "shirts")

auto.deposit(1000, "initial deposit")
auto.withdraw(15.89, "gas")

# Print individual categories
print("=" * 30)
print("FOOD CATEGORY")
print("=" * 30)
print(food)

print("\n" + "=" * 30)
print("CLOTHING CATEGORY")
print("=" * 30)
print(clothing)

print("\n" + "=" * 30)
print("AUTO CATEGORY")
print("=" * 30)
print(auto)

# Create and print spend chart
print("\n" + "=" * 30)
print("SPEND CHART")
print("=" * 30)
chart = create_spend_chart([food, clothing, auto])
print(chart)
