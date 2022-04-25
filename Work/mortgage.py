# mortgage.py
#
# Exercise 1.7

import argparse


def get_args():
    """Get command line args"""
    parser = argparse.ArgumentParser(
        description="Mortgage Calculator", formatter_class=ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "principal", type=float, help="principal amount", metavar="dollar amount"
    )
    parser.add_argument(
        "-r", "--rate", type=float, help="mortgage rate percentage", default="3.5"
    )

    args = parser.parse_args()
    return args
    # -------------------------------------------------------


def main():
    args = get_args()
    principal = 500000.0
    rate = 0.05
    payment = 2684.11
    total_paid = 0.0

    while principal > 0:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
    print(f"Total paid: ${total_paid:,.2f}")


if __name__ == "__main__":
    main()
