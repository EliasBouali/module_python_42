#!/usr/bin/env python3



def secure_archive(filename : str, action : str ="read", content : str ="") -> tuple[bool, str] :
    try :
        if action == "read" :
            with open(filename) as file :
                data = file.read()
            return (True, data)
        elif action == "write" :
            with open(filename, "w") as new_file :
                new_file.write(content)
            return (True, content)
        else :
            return (False, "nothing to do")
    except OSError :
        return (False, "Error: unable to read/write file")


def main() :
    result = secure_archive("test_1.txt", "write", "hello test 1")
    print(result)

    result = secure_archive("test_1.txt", "read")
    print(result)

if __name__ == "__main__" :
    main()
