import string
import sys

def text_analyzer(text="", ):
    """This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
    length = len(text)
    if length == 0:
        print("What is the text to analyse?")
        return text_analyzer(input())
    print("The text contains {} characters:\n".format(length))
    upper = 0
    for a in text:
        if (a.isupper() == True):
            upper +=  1
    print(" - {} upper letters\n".format(upper))
    lower = 0
    for a in text:
        if a.islower() == True:
            lower += 1
    print(" - {} lower letters\n".format(lower))
    punc = 0
    for a in text:
        if a in string.punctuation:
            punc += 1
    print(" - {} punctuation marks\n".format(punc))
    space = 0
    for a in text:
        if a.isspace():
            space += 1
    print(" - {} spaces".format(space))
