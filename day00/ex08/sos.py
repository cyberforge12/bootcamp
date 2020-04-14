import sys
import argparse
import string

sys.stderr = object
args_num = len(sys.argv)
if args_num == 1:
    exit(0)
ap = argparse.ArgumentParser()
ap.add_argument('str1', nargs="*", type=str)
try:
    args = ap.parse_args()
except Exception:
    print("ERROR")
    exit(1)

morse_dict = { 'A':'.-', 'B':'-...',
               'C':'-.-.', 'D':'-..', 'E':'.',
               'F':'..-.', 'G':'--.', 'H':'....',
               'I':'..', 'J':'.---', 'K':'-.-',
               'L':'.-..', 'M':'--', 'N':'-.',
               'O':'---', 'P':'.--.', 'Q':'--.-',
               'R':'.-.', 'S':'...', 'T':'-',
               'U':'..-', 'V':'...-', 'W':'.--',
               'X':'-..-', 'Y':'-.--', 'Z':'--..',
               '1':'.----', '2':'..---', '3':'...--',
               '4':'....-', '5':'.....', '6':'-....',
               '7':'--...', '8':'---..', '9':'----.',
               '0':'-----', ' ': '/'}


source = [i.upper() for i in args.str1]
s2 = ' '.join(i for i in source)
try:
    code = [morse_dict[i] for i in s2]
except Exception:
    print("ERROR")
    exit(1)
for i in code:
    print(i, end=' ')
print("")

