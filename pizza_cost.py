#!/usr/bin/env python3

# Created by: Mignonne Gihozo
# Created on: September 2026
# This program calculates the area, perimeter, and total cost of a pizza.

import math
import constants


def main():
    # Input
    diameter = float(input("Enter the diameter of the pizza (inches): "))

    # Process (Geometric Calculations)
    radius = diameter / 2
    area = math.pi * (radius**2)
    perimeter = math.pi * diameter

    # Process (Cost Calculations)
    subtotal = (
        constants.LABOUR_COST
        + constants.RENTAL_COST
        + (constants.INGRED_COST * diameter)
    )
    tax = constants.HST * subtotal
    total = subtotal + tax

    # Output
    print("")
    print(f"The area of the pizza is: {area:.2f} square inches.")
    print(f"The perimeter (circumference) of the pizza is: {perimeter:.2f} inches.")
    print(f"The total cost is: ${total:.2f}")


if __name__ == "__main__":
    main()
