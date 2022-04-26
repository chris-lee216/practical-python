# mortgage.py
#
# Author: Chris Lee
# Date: April 25, 2022
# Exercise 1.7

import argparse


def get_args():
    """Get command line args"""
    parser = argparse.ArgumentParser(
        description="Mortgage Calculator",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "principal", type=float, help="principal amount", metavar="dollar amount"
    )
    parser.add_argument(
        "-r", "--rate", type=float, help="mortgage rate percentage", default="3.5"
    )

    parser.add_argument("-e", "--extra", type=float, help="extra payment", default=0.0)
    parser.add_argument(
        "-s",
        "--start",
        type=int,
        help="extra payment start month",
        metavar="MONTH",
        default=1,
    )
    parser.add_argument(
        "-E",
        "--end",
        type=int,
        help="extra payment end month",
        metavar="MONTH",
        default=12,
    )

    args = parser.parse_args()
    return args


# ----------------------------------------------------------------------------------------


def calc_payment(principal, rate, payment, extra_payment, start, end):
    """calculate monthly payments"""
    total_paid = 0.0
    month = 1
    while principal > 0:
        if month >= start and month < end:
            principal = principal * (1 + rate / 12) - (payment + extra_payment)
            total_paid = total_paid + payment + extra_payment
        else:
            principal = principal * (1 + rate / 12) - (payment)
            total_paid = total_paid + payment
        print(f"{month} ${total_paid:,.2f} ${principal:,.2f}")
        month += 1
    print(f"Total paid: ${total_paid:,.2f}")
    print(f"Months: {month}")


# ----------------------------------------------------------------------------------------


def main():
    """It starts here..."""
    args = get_args()
    principal = args.principal
    rate = args.rate / 100
    payment = 2684.11
    total_paid = 0.0
    extra_payment = args.extra
    start = args.start
    end = args.end + 1
    calc_payment(principal, rate, payment, extra_payment, start, end)


if __name__ == "__main__":
    main()
