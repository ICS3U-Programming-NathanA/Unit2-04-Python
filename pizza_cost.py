#!/usr/bin/env python3
# Created by: Nathan Araujo
# Created on: Sept 28 2022
# This program asks the user for the diameter of the
# pizza. It then calculates and displays the total cost
# of the pizza with tax
import constants


def main():

    # Get the input for the diameter of the pizza
    diameter = float(input("Enter the diameter of the pizza in inches: "))

    # Calculate the total for the diameter of the pizza
    subtotal = (
        constants.LABOUR_COST + constants.RENTAL_COST + constants.INGRED_COST * diameter
    )
    tax = subtotal * constants.HST
    total = subtotal + tax

    # Display the results
    print("")
    print("The total for the pizza is ${:.2f}".format(total))


if __name__ == "__main__":
    main()
