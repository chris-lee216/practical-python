# pcost.py
#
# Author: Chris Lee
# Date: April 30, 2022
# Exercise 2.4,2.5,2.6,2.7

import csv


def portfolio_cost(file_path):
    """Return the cost of a portfolio"""
    total_cost = 0
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        # for row in reader:
        portfolio = {
            row.get("name"): {
                "shares": int(row.get("shares")),
                "price": float(row.get("price")),
            }
            for row in reader
        }
    return portfolio


# ----------------------------------------------------------------------------------------
def read_prices(file_path):
    """read stock prices from csv into dictionary"""
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=["name", "price"])
        stock_prices = {row.get("name"): float(row.get("price")) for row in reader}
    return stock_prices


# ----------------------------------------------------------------------------------------
def make_report(portfolio, stock_prices):
    """generate report"""
    report_data = []
    # this could be done using a list comprehension, but readability would be sacrificed.
    for row in portfolio:
        current_price = stock_prices[row]
        purchase_price = portfolio[row]["price"]
        change = current_price - purchase_price
        shares = portfolio[row]["shares"]
        report_data.append((row, shares, current_price, change))
    return report_data


# ----------------------------------------------------------------------------------------
def print_report(report_data):
    """Print report using the list of tuples"""
    headers = ("Name", "Shares", "Price", "Change")
    lines = "---------- ---------- ---------- -----------"
    print(
        "{:>10} {:>10} {:>10} {:>10}".format(
            headers[0], headers[1], headers[2], headers[3]
        )
    )
    print("{:>10}".format(lines))
    dollar = "$"
    for name, shares, price, change in report_data:
        print(f"{name:>10s} {shares:>10d} {price:10.2f} {change:>10.2f}")


# ----------------------------------------------------------------------------------------
def main():
    """It starts here"""
    portfolio_path = "Data/portfolio.csv"
    prices_path = "Data/prices.csv"
    portfolio = portfolio_cost(portfolio_path)
    stock_prices = read_prices(prices_path)

    report_data = make_report(portfolio, stock_prices)
    print_report(report_data)


if __name__ == "__main__":
    main()
