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
        print(f"{filename}")
        print(f"{data}")
        file.close()
    except OSError :
        print(f"{filename}")
        print("Error: unable to read file")
        return 

if __name__ == "__main__" :
    main()
