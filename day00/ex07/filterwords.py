import string
import sys
import argparse

sys.stderr = object
args_num = len(sys.argv)
if args_num > 3:
    print("ERROR")
    exit(1)
if args_num == 1:
    exit(0)
ap = argparse.ArgumentParser()
ap.add_argument('str1', nargs=1, type=str)
ap.add_argument('int1', nargs=1, type=int)
try:
    args = ap.parse_args()
except Exception:
    print("ERROR")
    exit(1)
if args.str1[0].isdigit():
    print("ERROR")
    exit(1)
str1 = args.str1[0].translate(args.str1[0].maketrans('', '', string.punctuation))
new_t = [i for i in str1.split(sep=' ') if len(i) > args.int1[0]]
print(new_t)