from sre_parse import SPECIAL_CHARS
from Crypto.Cipher import DES,AES
from Crypto.Random import get_random_bytes
import math
from sys import argv

from click import password_option
from entropy import count_entropy_of_text
from Crypto.Util.Padding import pad
import string
from Crypto.Protocol.KDF import PBKDF2

def max_info_in_sign(n):
    return math.log2(n)

def max_entropy_in_text(k, n):
    return k*max_info_in_sign(n)

LOWERCASE_LETTERS = list(string.ascii_lowercase)
UPPERCASE_LETTERS = list(string.ascii_uppercase)
SPECIAL_CHARS = list(string.punctuation)

def count_length_of_alphabet(key):
    alph_lenght = 0
    check_letters = {"lowercase" : False, "uppercase": False, "special" : False}
    for sign in key:
        if sign in LOWERCASE_LETTERS:
            check_letters["lowercase"] = True
        if sign in UPPERCASE_LETTERS:
            check_letters["uppercase"] = True
        if sign in SPECIAL_CHARS:
            check_letters["special"] = True
    
    if check_letters["lowercase"] == True:
        alph_lenght += len(LOWERCASE_LETTERS)
    if check_letters["uppercase"] == True:
        alph_lenght += len(UPPERCASE_LETTERS)
    if check_letters["special"] == True:
        alph_lenght += len(SPECIAL_CHARS)

    return alph_lenght


# Comparing entropy - ECB and CBC mode
t = ""
for i in range(9999):
    t += "0"

key = "key4567890123456"

if len(argv) == 3:
    file = open(argv[1], "r")  # encrypted text
    t = file.read()
    key = argv[2]

BLOCK_SIZE = 16
key = PBKDF2(str.encode(key), BLOCK_SIZE)

aes_ecb = AES.new(key, AES.MODE_ECB)
encrypted = aes_ecb.encrypt(pad(str.encode(t), BLOCK_SIZE))

print("AES ECB entropy: {}".format(count_entropy_of_text(encrypted)))

iv = get_random_bytes(16)
aes_cbc = AES.new(key, AES.MODE_CBC, iv)
encrypted = aes_cbc.encrypt(pad(str.encode(t), BLOCK_SIZE))

print("AES CBC entropy: {}".format(count_entropy_of_text(encrypted)))

# print(count_entropy_of_text(t))

password_entropy = len(argv[2])*math.log2(count_length_of_alphabet(argv[2]))
print("Entropy of password: {}".format(password_entropy))

if(password_entropy >= 100):
    f = open(argv[3], "wb")
    f.write(encrypted)
    f.close
    print("File encrypted")
else:
    print("Entropy of your password is too low!")