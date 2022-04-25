#!/usr/bin/env python3
# bounce.py
#
# Author: Chris Lee
# Exercise 1.5

import argparse
import pytest

# -------------------------------------------------------
def get_args():
    """Get command line args"""
    parser = argparse.ArgumentParser(
        "Simulate ball drop", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-n", "--number", metavar="int", type=int, default=10, help="number of bounces"
    )

    parser.add_argument(
        "-H",
        "--height",
        metavar="int",
        type=float,
        default=60.0,
        help="height of initial drop",
    )
    args = parser.parse_args()
    return args


# -------------------------------------------------------
def bounce(height, bounce_back):
    """bounce dat..."""
    return height * bounce_back


# -------------------------------------------------------
def test_bounce():
    assert bounce(60.0, 0.6) == 36.0
    assert bounce(36.0, 0.6) == 21.599999999999998


# -------------------------------------------------------


def main():
    """Its just begun"""
    args = get_args()
    bounce_back = 0.6  # 3/5
    num_bounces = args.number
    height = args.height
    for i in range(1, num_bounces + 1):
        print(f"{i:2} {round(height, 4):.4f}")
        height = bounce(height, bounce_back)


# -------------------------------------------------------
if __name__ == "__main__":
    main()
