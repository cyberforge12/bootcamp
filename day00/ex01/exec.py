import sys

length = len(sys.argv)
if length > 1:
	while length > 1:
		newtxt = ""
		txt = sys.argv[length - 1][::-1]
		for a in txt:
			if (a.isupper() == True):
				newtxt += a.lower()
			else:
				newtxt += a.upper()
		print(newtxt, end="")
		if length != 2:
			print(end=" ")
		length -= 1
	print()
