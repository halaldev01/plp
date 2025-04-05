def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if final_price != price:
        print(f"Discount applied! The final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
