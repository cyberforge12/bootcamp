import time
import numpy as np

def randbelow(n):
    return (7 * time.time() + 11) % n

def generator(text, sep=" ", option=None):
    """Option is an optional arg, sep is mandatory"""
    if type(text) == str:
        txt = text.split(sep)
        if option == "shuffle":
            for i in reversed(range(1, len(txt))):
            # pick an element in text[:i+1] with which to exchange x[i]
                j = int(randbelow(i + 1))
                txt[i], txt[j] = txt[j], txt[i]
        elif option == "ordered":
            return sorted(txt, key=str.casefold)
        elif option == "unique":
            return np.unique(np.array(txt))
        elif option not in [None, 'unique', 'ordered', 'shuffle']:
            return ["ERROR"]
        return txt
    else:
        return ["ERROR"]
