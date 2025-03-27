import sys


try:
    try:
        if len(sys.argv) < 2:
            exit()
        num = int(sys.argv[1])
    except ValueError:
        raise AssertionError("Argument is not an integer")
    if len(sys.argv) != 2:
        raise AssertionError("Incorrect number of arguments")

    if int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


except AssertionError as error:
    print(AssertionError.__name__ + ":", error)
