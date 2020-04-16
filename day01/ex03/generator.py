# function prototype
import struct
import time

def randbelow(n):
    return (7 * time.time() + 11) % n

def generator(text, sep=" ", option=None):
    """Option is an optional arg, sep is mandatory"""
    txt = text.split(sep)
    if option == "shuffle":
        for i in reversed(range(1, len(txt))):
        # pick an element in text[:i+1] with which to exchange x[i]
            j = int(randbelow(i + 1))
            txt[i], txt[j] = txt[j], txt[i]
    elif option == "ordered":
        return sorted(txt, key=str.casefold)
    return txt

text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" "):
    print(word)

print("\nshuffle:")
for word in generator(text, sep=" ", option="shuffle"):
    print(word)

print("\nordered:")
for word in generator(text, sep=" ", option="ordered"):
    print(word)
