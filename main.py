#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: March 3, 2025
# DESCRIPTION HERE
import code_gen
import output_handler


def main():
    # Greetings

    # INPUT
    # Ask User for amount of sides in the base
    side_amount = int(input("Enter the amount of Sides in the base: "))
    # Ask User for type of shape (prism/pyramid)
    shape_type = input("Type? (Prism/Pyramid): ")
    # Ask User for the unit Type
    unit_type = input("Units? (cm,km,mm,etc.): ")

    # Generating the code
    generated_code = code_gen.get_code(side_amount, shape_type, unit_type)

    # OUTPUT
    output_handler.addCodeToFile(generated_code)
    print("DONE!")

    pass


if __name__ == "__main__":
    main()
