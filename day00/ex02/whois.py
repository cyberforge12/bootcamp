import sys
import argparse

sys.stderr = object
len = len(sys.argv)
if len > 1:
	ap = argparse.ArgumentParser(description = 'Returns a type of an integer argument')
	ap.add_argument('ints', nargs = 1, type = int, help = 'an integer')
	try:
		args = ap.parse_args()
	except Exception:
		print("ERROR")
		exit(0)
	i = args.ints[0]
	if i == 0:
		print("I'm Zero")
	elif i % 2 == 0:
		print("I'm Even")
	else:
		print("I'm Odd")
