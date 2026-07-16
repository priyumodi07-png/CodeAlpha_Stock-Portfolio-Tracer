
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOGL": 140,
    "AMZN": 130
}

# Empty portfolio to be filled by user input
portfolio = {}

# Ask user how many stocks they want to add
n = int(input("How many different stocks do you want to add? "))

for i in range(n):
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    qty = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = qty

# Initialize total value and lines for file
total_value = 0
lines = []
lines.append("Portfolio Summary:\n")

# Calculate value for each stock
for stock, qty in portfolio.items():
    if stock in stock_prices:  # safety check
        value = stock_prices[stock] * qty
        total_value += value
        lines.append(f"{stock}: {qty} shares -> ${value}\n")
    else:
        lines.append(f"{stock}: Price not available\n")

# Add total investment value
lines.append(f"\nTotal Investment Value: ${total_value}\n")

# Save to file
file_path = "portfolio.txt"
with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"Portfolio saved to {file_path}")
