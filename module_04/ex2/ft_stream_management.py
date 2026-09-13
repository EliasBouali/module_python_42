#!/usr/bin/env python3

import sys

def main() :
    if len(sys.argv) != 2 :
        sys.stderr.write(f"number of arguments required : 1\n")
        sys.stderr.write(f"current number of arguments : {len(sys.argv) - 1}\n")
        return

    filename = sys.argv[1]

    try :
        file = open(filename)
        data = file.read()
        print("=== Cyber Archives Recovery ===")
        file.close()
    except OSError :
        sys.stderr.write(f"{filename}\n")
        sys.stderr.write("Error: unable to read file\n")
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

    new_filename = sys.stdin.readline()
    if new_filename and  new_filename[-1] == "\n" :
        new_filename = new_filename[:-1]
    if not new_filename:
        return
    else :
        try:
            new_file = open(new_filename, "w")
            new_file.write(new_data)
            new_file.close()
        except OSError :
            sys.stderr.write("Error: unable to write file\n")

if __name__ == "__main__" :
    main()
