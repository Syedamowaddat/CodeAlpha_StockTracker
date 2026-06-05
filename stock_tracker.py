# ========================================
# STOCK PORTFOLIO TRACKER
# CodeAlpha Python Internship
# Author: Syeda Mowaddat Zahra Naqvi
# ========================================

import os
import csv
# ---- CLEAR SCREEN ----
def clear_screen():
    os.system('clear')

# ---- STOCK PRICES ----
STOCKS = {
    "AAPL":  180,
    "TSLA":  250,
    "GOOGL": 140,
    "AMZN":  175,
    "MSFT":  380,
    "META":  300,
    "NFLX":  450,
    "NVDA":  500,
    "UBER":  60,
    "PYPL":  65
}
# ---- SHOW AVAILABLE STOCKS ----
def show_stocks():
    clear_screen()
    print("=" * 45)
    print("   📈 STOCK PORTFOLIO TRACKER | CodeAlpha")
    print("=" * 45)
    print(f"\n  {'Stock':<8} {'Company':<12} {'Price':>10}")
    print("  " + "-" * 35)
    
    companies = {
        "AAPL":  "Apple",
        "TSLA":  "Tesla",
        "GOOGL": "Google",
        "AMZN":  "Amazon",
        "MSFT":  "Microsoft",
        "META":  "Meta",
        "NFLX":  "Netflix",
        "NVDA":  "Nvidia",
        "UBER":  "Uber",
        "PYPL":  "PayPal"
    }
    
    for stock, price in STOCKS.items():
        company = companies[stock]
        print(f"  {stock:<8} {company:<12} ${price:>8}")
    
    print("=" * 45)
    
# ---- SHOW PORTFOLIO ----
def show_portfolio(portfolio):
    print("\n" + "=" * 45)
    print("   💼 YOUR PORTFOLIO SUMMARY")
    print("=" * 45)
    print(f"  {'Stock':<8} {'Price':<10} {'Qty':<6} {'Total':<10} {'Share'}")
    print("  " + "-" * 40)
    
    grand_total = 0
    for stock, qty in portfolio.items():
        price = STOCKS[stock]
        total = price * qty
        grand_total += total

    for stock, qty in portfolio.items():
        price = STOCKS[stock]
        total = price * qty
        percent = (total / grand_total) * 100
        print(f"  {stock:<8} ${price:<9} {qty:<6} ${total:<9} {percent:.1f}%")
    
    print("  " + "-" * 40)
    print(f"\n  💰 Total Investment: ${grand_total}")
    
    # Best stock
    best = max(portfolio, key=lambda s: STOCKS[s])
    print(f"  📈 Highest Price Stock: {best}")
    
    # Most invested
    most = max(portfolio, key=lambda s: STOCKS[s]*portfolio[s])
    print(f"  💹 Most Invested: {most}")
    print("=" * 45)
 
 # ---- SAVE TO CSV ----
def save_portfolio(portfolio):
    with open("portfolio.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Price", 
                         "Quantity", "Total"])
        grand_total = 0
        for stock, qty in portfolio.items():
            price = STOCKS[stock]
            total = price * qty
            grand_total += total
            writer.writerow([stock, f"${price}", 
                            qty, f"${total}"])
        writer.writerow(["", "", "TOTAL", 
                        f"${grand_total}"])
    print("\n  ✅ Portfolio saved to portfolio.csv!")

# ---- MAIN FUNCTION ----
def main():
    portfolio = {}
    
    while True:
        show_stocks()
        print("\n  OPTIONS:")
        print("  1 → Add Stock")
        print("  2 → View Portfolio")
        print("  3 → Save & Exit")
        
        choice = input("\n  Enter choice (1/2/3): ")
        
        if choice == "1":
            stock = input("\n  Enter stock name: ").upper()
            if stock not in STOCKS:
                print("  ❌ Invalid stock!")
                continue
            try:
                qty = int(input("  Enter quantity: "))
                if qty <= 0:
                    print("  ❌ Invalid quantity!")
                    continue
                if stock in portfolio:
                    portfolio[stock] += qty
                else:
                    portfolio[stock] = qty
                print(f"  ✅ {stock} x{qty} added!")
            except ValueError:
                print("  ❌ Enter numbers only!")
                
        elif choice == "2":
            if not portfolio:
                print("  ❌ Portfolio empty!")
            else:
                show_portfolio(portfolio)
            input("\n  Press Enter to continue...")
            
        elif choice == "3":
            if portfolio:
                show_portfolio(portfolio)
                save_portfolio(portfolio)
            print("\n  Thanks! CodeAlpha Internship")
            break

# ---- START ----
main()
