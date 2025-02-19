# Asks the user for the number of items purchased
item_count = int(input("How many items have you purchased? "))

# Initializes an empty list to store item prices
prices = []

# Loops through to get the price of each product
for item in range(item_count):
    price = float(input(f"Please enter the price of product {item + 1}: "))
    prices.append(price)  # Stores price in the prices list

# Calculates the total cost by summing up the list
total_cost = sum(prices)

# Display the stored prices and total cost
print("\nYou have entered the following prices:", prices)
print(f"The total cost of the products you have purchsed is Ksh {total_cost:.2f}")
