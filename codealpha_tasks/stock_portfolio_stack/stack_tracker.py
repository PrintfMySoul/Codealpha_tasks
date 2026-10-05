stock_prices= {
    "AAPL": 180, 
    "TSLA": 250,
    "MSFT": 420,
    "GOOG": 160
}
total_investment = 0
while True:
    stock = input("Enter stock name: ").upper()
    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
    
        investment = quantity * stock_prices[stock]
        total_investment += investment
    
        print(f"{stock}: {quantity} shares * ${stock_prices[stock]}= ${investment} ")
    
        
    else:
        print("Stock not found. Please enter a valid stock name.")


    answer =input("Do you want to continue? (yes/no): ").lower()
    if answer != "yes":
        break

print(f"Total investment: ${total_investment}")

with open("portfolio.txt", "w") as file:
    file.write(f"Total investment :${total_investment}")