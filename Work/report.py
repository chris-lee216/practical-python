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
            row.get("name"): {"shares": row.get("shares"), "price": row.get("price")}
            for row in reader
        }
        # names = int(row.get("names"))
        # price = float(row.get("price"))
        # total_cost += names * price
    return portfolio


# ----------------------------------------------------------------------------------------
def read_prices(file_path):
    """read stock prices from csv into dictionary"""
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=["name", "price"])
        stock_prices = {row.get("name"): float(row.get("price")) for row in reader}
    return stock_prices


# ----------------------------------------------------------------------------------------
def main():
    """It starts here"""
    file_path = "Data/prices.csv"
    # total_cost = portfolio_cost(file_path)
    # print(f"Total cost: ${total_cost:,.2f}")


if __name__ == "__main__":
    main()
