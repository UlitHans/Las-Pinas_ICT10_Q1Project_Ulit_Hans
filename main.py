from pyscript import display
# Restaurant Ordering System using Python

# String Data Type
restaurant_name = "boss_seth's kitchen"
owner_name = "Hans Ulit"

# Integer Data Type
year_since = 2025

# Float Data Type
tax_rate = 0.08

# Boolean Data Type
has_deliver = True
is_dine_in = True
is_takeaway = False

# List Data Type
products = ["Burger", "Pizza", "Pasta", "Salad", "Soda"]

# Tuple Data Type
business_hours = ("Mon-Fri: 9am-9pm", "Sat-Sun: 10am-8pm")

# Dictionary Data Type
menu = {
    "Burger": 79.99,
    "Pizza": 150.00,
    "Pasta": 120.50,
    "Salad": 49.99,
    "Soda": 19.99
}

# Set Data Type
allergens = {"nuts", "dairy", "gluten"}

# Displaying restaurant Information
display(f"{restaurant_name}", target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since: {year_since}", target="since")
display(f"Menu Pricelist", target="heading1")

# Display Menu Items
display(products[0], target="prod1")
display(f"₱{menu['Burger']:.2f}", target="price1")
display(products[1], target="prod2")
display(f"₱{menu['Pizza']:.2f}", target="price2")
display(products[2], target="prod3")
display(f"₱{menu['Pasta']:.2f}", target="price3")
display(products[3], target="prod4")
display(f"₱{menu['Salad']:.2f}", target="price4")
display(products[4], target="prod5")
display(f"₱{menu['Soda']:.2f}", target="price5")

#Opening Hours Target
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")

# Display order type
display(f"Dine-in Available", target="orderType")