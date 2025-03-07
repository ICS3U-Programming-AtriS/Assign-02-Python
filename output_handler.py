#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: March 3, 2025
# This module is in charge of creating the output file that contains the code

output_file_path = (
    "/home/vscode/ICS3U/Assign/Assign-02/Assign-02-Python/OUTPUT/output_code.py"
)


def addCodeToFile(code: str):
    with open(output_file_path, "r+") as file:
        # Delete all contents of file
        file.truncate(0)
        # Add the Code to the file
        file.write(code)
        # Close the file
        file.close()
