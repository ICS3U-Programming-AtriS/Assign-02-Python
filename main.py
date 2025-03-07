#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: March 3, 2025
# Main file for the Calculator Calculator
import code_gen
import output_handler


# Input Validation
def int_input(prompt: str, minimum=0):
    # Keep Looping until input is valid
    while True:
        try:
            print("\033[0m", end="")  # WHITE TEXT
            res = int(input(prompt))
            if res >= minimum:
                return res
            else:
                print("\033[0;31m", end="")  # RED TEXT
                print(f"Value must be greater than or equal to than {minimum}")
        except ValueError:
            print("\033[0;31m", end="")  # RED TEXT
            print("Value must be a positive integer")


def get_shape_type(prompt: str, options):
    while True:
        print("\033[0m", end="")  # WHITE TEXT
        res = input(prompt)
        if res.lower() in options:
            return res.capitalize()
        else:
            print("\033[0;31m", end="")  # RED TEXT
            print("Not a valid option!")


def main():
    # Welcome Message
    print("\033[0;34m", end="")  # BLUE TEXT
    print("Welcome to the", end=" ")
    print("NSRPCPFBWAMNSRPCPTSAPIOOTTVOAPWTSDAABMPCPLTHMTMPCP", end=" ")
    print("(N-Sided Regular Prism Calculator Program Factory", end=" ")
    print("But We Also Make N-Sided Pyramid Calculator Programs Too", end=" ")
    print("Since A Pyramid Is Only One Third The Volume", end=" ")
    print("Of A Prism With The Same Dimensions And Also Because", end=" ")
    print("Pyramid Calculator Programs Leads To Higher Margins", end=" ")
    print("Than Making Prism Calculator Programs)!", end=" ")
    print("Let's make a calculator program!")
    # INPUT
    # Ask User for amount of sides in the base
    side_amount = int_input("Enter the amount of sides in the base: ", 3)
    # Ask User for type of shape (prism/pyramid)
    shape_type = get_shape_type("Type? (Prism/Pyramid): ", ["prism", "pyramid"])
    # Ask User for the unit Type [It can be anything]
    unit_type = input("Units? (cm,km,mm,etc.): ")

    # Generate the code
    generated_code = code_gen.get_code(side_amount, shape_type, unit_type)

    # OUTPUT
    output_handler.addCodeToFile(generated_code)
    print("DONE!")


if __name__ == "__main__":
    main()
