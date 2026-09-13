#!/usr/bin/env python3

import sys

def main() :
    if len(sys.argv) != 2 :
        print(f"number of arguments required : 1")
        print(f"current number of arguments : {len(sys.argv) - 1}")
        return

    filename = sys.argv[1]

    try :
        file = open(filename)
        data = file.read()
        print("=== Cyber Archives Recovery ===")
        file.close()
    except OSError :
        print(f"{filename}")
        print("Error: unable to read file")
        return

    print(f"{filename}")
    print(f"{data}")

    new_data = ""

    for letter in data :
        if letter == "\n" :
            new_data += "#"
            new_data += "\n"
        else :
            new_data += letter

    new_data += "#"
    print(f"{new_data}")

    new_filename = input("name of the file to save: ")
    if not new_filename:
        return
    else :
        try:
            new_file = open(new_filename, "w")
            new_file.write(new_data)
            new_file.close()
        except OSError :
            print("Error: unable to write file")

if __name__ == "__main__" :
    main()
