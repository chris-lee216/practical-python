# pcost.py
#
# Author: Chris Lee
# Date: April 28, 2022
# Exercise 1.27

import csv


def portfolio_cost(path):
    """Return the cost of a portfolio"""
    total_cost = 0
    with open(path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            shares = int(row.get("shares"))
            price = float(row.get("price"))
            total_cost += shares * price
    return total_cost


# ----------------------------------------------------------------------------------------
def main():
    """It starts here"""
    path = "Data/portfolio.csv"
    total_cost = portfolio_cost(path)
    print(f"Total cost: ${total_cost:,.2f}")


if __name__ == "__main__":
    main()
