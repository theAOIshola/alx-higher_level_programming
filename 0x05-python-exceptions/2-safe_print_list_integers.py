#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    index = 0
    for x in range(x):
        try:
            print("{:d}".format(my_list[x]), end="")
            index += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (index)
