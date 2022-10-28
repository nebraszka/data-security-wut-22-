import math
import string

def max_info_in_sign(n):
    return math.log2(n)

def max_entropy_in_text(k, n):
    return k*max_info_in_sign(n)

LOWERCASE_LETTERS = list(string.ascii_lowercase) 
UPPERCASE_LETTERS = list(string.ascii_uppercase)
SPECIAL_CHARS = list(string.punctuation)
NUMBERS = list(string.digits)

def count_length_of_alphabet(key):
    alph_lenght = 0
    check_letters = {"lowercase" : False, "uppercase": False, "special" : False, "numbers": False}
    for sign in key:
        if sign in LOWERCASE_LETTERS:
            check_letters["lowercase"] = True
        if sign in UPPERCASE_LETTERS:
            check_letters["uppercase"] = True
        if sign in SPECIAL_CHARS:
            check_letters["special"] = True
        if sign in NUMBERS:
            check_letters["numbers"] = True
    
    if check_letters["lowercase"] == True:
        alph_lenght += len(LOWERCASE_LETTERS)
    if check_letters["uppercase"] == True:
        alph_lenght += len(UPPERCASE_LETTERS)
    if check_letters["special"] == True:
        alph_lenght += len(SPECIAL_CHARS)
    if check_letters["numbers"] == True:
        alph_lenght += len(NUMBERS)

    return alph_lenght