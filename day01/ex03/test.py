from generator import generator

text = "Le Lorem Ipsum est simplement du faux texte. Repeat Repeat Repeat"
print("\nno option:")
for word in generator(text, sep=" "):
    print(word)

print("\nshuffle:")
for word in generator(text, sep=" ", option="shuffle"):
    print(word)

print("\nordered:")
for word in generator(text, sep=" ", option="ordered"):
    print(word)

print("\nunique:")
for word in generator(text, sep=" ", option="unique"):
    print(word)
print("\nsep=\".\":")
for word in generator(text, sep="."):
    print(word)
print("\nERROR option:")
for word in generator(text, sep=" ", option="ERROR"):
    print(word)
print("\nERROR text:")
for word in generator(12312312, sep=" ", option="unique"):
    print(word)
