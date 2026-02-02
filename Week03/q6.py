print("=" * 50)
print("Question 6: Inventory Management System")
print("=" * 50)

# 1. Create inventory dictionary with tuples as values
inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8)
}

# 2. Print inventory using for loop with items()
print("=== Current Inventory ===")
for product, details in inventory.items():
    price = details[0]
    quantity = details[1]
    print(product + " - Price: $" + str(price) + ", Quantity: " + str(quantity))

print()

# 3. Create category sets
electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}

# 4. Find all products using union
all_products = electronics | accessories
print("All product categories:", all_products)

print()
