#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: March 3, 2025
# This module is in charge of creating the output file that contains the code

# File path to the file that will get the generated code
output_file_path = "/home/vscode/ICS3U/Assign/Assign-02/"
output_file_path += "Assign-02-Python/OUTPUT/output_code.py"


# Function that adds the code to the output file
def addCodeToFile(code: str):
    with open(output_file_path, "r+") as file:
        # Delete all contents of file
        file.truncate(0)
        # Add the Code to the file
        file.write(code)
        # Close the file
        file.close()
