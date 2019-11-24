#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: November 2019
# This program uses user defined functions


def calculate_area(base, height):
    # this function calculates area

    # process
    area = (base * height) / 2

    # output
    print ("")
    print("The area is {:,.2f} cm²"
          .format(area))


def main():
    # this function gets length and width and calls functions

    # input
    base_from_user = input("Enter the base of a triangle (cm): ")
    height_from_user = input("Enter the height of a triangle (cm): ")
    print("")

    try:
        base_from_user = float(base_from_user)
        height_from_user = float(height_from_user)
        calculate_area(base_from_user, height_from_user)
    except Exception:
        print("")
        print("Please insert a valid number.")


if __name__ == "__main__":
    main()
