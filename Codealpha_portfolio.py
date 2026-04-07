
# Dictinory storing predefined stock prices (in Rs)
stock_prices ={ 
    "AAPL": 180,     # Apple
    "GOOGL": 2800,   # Google
    "MSFT": 300,     # Microsoft
    "TSLA": 900,     # Tesla
    "AMZN": 3500,    # Amazon
}

# Display Welcome message
print("Welcome to stock portfolio Tracker")

# Show available stock symbols
print("Availble stocks:", ",".join(stock_prices.keys()))

# Dictinory to store user's portfolio(stock + quantity)
portfolio = {}

# Variable to store total portfolio value
total_value = 0

# Take input: how many different stocks user has
n = int(input("How many different stocks do you have? "))

# Loop to take stock inputs
for i in range(n):
    # Take stock exists in predefined list
    stock = input(f"\nEnter stock symbol #{i+1}: ").upper()
    if stock not in stock_prices:
        print("stock not found in database! Please enter a valid stock symbol.")
        continue  # Skip this ireation and move to next

    # Take quantity of that stock
    quantity = int(input(f"Enter quantity of {stock}: "))

    # Store stock and quantity of that stock
    portfolio[stock] = quantity

# Display portfolio summary
print("\n Your portfolio summary:")
# Loop through portfolio to calculate values
for stock, qty in portfolio.items():
  price = stock_prices[stock]  # get price of stock
  value = price * qty  # calculate total value of that stock 
  total_value += value  # add to total portfolio value

  # Print stock details
  print(f"{stock}: {qty} shares * ₹ {price} = ₹{value}")

# Print final total portfolio value
print(f"\nTotal portfolio value: ₹{total_value}")
