#!/usr/bin/env python3
# bounce.py
#
# Author: Chris Lee
# Exercise 1.5

import argparse


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
        "-h",
        "--height",
        metavar="int",
        type=int,
        default=60,
        help="height of initial drop",
    )
    args = parser.parse_args()
    return args


# -------------------------------------------------------
def bounce(num, height):
    """bounce dat..."""
# -------------------------------------------------------
def main():
    """Its just begun"""
    args = get_args()
    bounce_back = 0.6  # 3/5
    num_bounces = args.number
    starting_height = args.height



# -------------------------------------------------------
if __name__ == "__main__":
    main()
