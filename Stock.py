# CodeAlpha Task 2 - Stock Portfolio Tracker

stocks = {
    "INFY": 1650,
    "TCS": 3850,
    "RELIANCE": 2950,
    "WIPRO": 520,
    "HCLTECH": 1750
}

total_investment = 0

print("=== Stock Portfolio Tracker ===")
print("Available Stocks:", ", ".join(stocks.keys()))

while True:
    stock_name = input("\nEnter Stock Name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter Quantity: "))
        investment = stocks[stock_name] * quantity
        total_investment += investment

        print(f"{stock_name} Investment Value: ₹{investment}")
    else:
        print("Stock not found!")

print("\n===== Portfolio Summary =====")
print(f"Total Investment Value: ₹{total_investment}")

# Save result to file
with open("portfolio_report.txt", "w") as file:
    file.write(f"Total Investment Value: ₹{total_investment}")

print("Portfolio report saved as 'portfolio_report.txt'")
