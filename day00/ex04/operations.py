import argparse
import sys


def summarize(x: int, y: int) -> int:
    total = x + y
    print("Sum:\t\t", total)
    return total


def substract(x: int, y: int) -> int:
    total = x - y
    print("Difference:\t", total)
    return total


def product(x: int, y: int) -> int:
    total = x * y
    print("Product:\t", total)
    return total


def divide(x: int, y: int) -> int:
    try:
        total = x / y
        print("Quotient:\t", total)
        return total
    except ZeroDivisionError:
        print("Quotient:\t", "ERROR (div by zero)")


def modulo(x: int, y: int) -> int:
    try:
        total = x % y
        print("Remainder:\t", total)
        return total
    except ZeroDivisionError:
        print("Remainder:\t", "ERROR (modulo by zero)")


def msg(name=None):
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("\tpython operations.py 10 3")


sys.stderr = object
args_num = len(sys.argv)
if args_num > 3:
    print("InputError: too many arguments\n")
    msg()
    exit(1)
use_msg = "Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3"
ap = argparse.ArgumentParser(usage=use_msg)
ap.add_argument('int1', nargs=2, type=int)
try:
    args = ap.parse_args()
except Exception:
    print("InputError: only numbers\n")
    print(use_msg)
    exit(1)
int1 = args.int1[0]
int2 = args.int1[1]
summarize(int1, int2)
substract(int1, int2)
product(int1, int2)
divide(int1, int2)
modulo(int1, int2)
