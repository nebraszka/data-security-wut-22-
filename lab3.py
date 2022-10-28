# Comparing entropy - ECB and CBC mode

from venv import create
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from sys import argv
from entropy import count_entropy_of_text
from Crypto.Util.Padding import pad
from Crypto.Protocol.KDF import PBKDF2
from lab3functions import max_entropy_in_text, count_length_of_alphabet

# default text to encrypt with entropy ~ 0
t = ""
for i in range(9999):
    t += "0"

# default key
key = "key4567890123456"

if len(argv) > 1:
    file = open(argv[1], "r")  # encrypted text
    t = file.read()

if len(argv) > 2:
    key = argv[2]

BLOCK_SIZE = 16
key_modified = PBKDF2(str.encode(key), BLOCK_SIZE)

aes_ecb = AES.new(key_modified, AES.MODE_ECB)
encrypted = aes_ecb.encrypt(pad(str.encode(t), BLOCK_SIZE))

print("AES ECB entropy: {}".format(count_entropy_of_text(encrypted)))

iv = get_random_bytes(16)
aes_cbc = AES.new(key_modified, AES.MODE_CBC, iv)
encrypted = aes_cbc.encrypt(pad(str.encode(t), BLOCK_SIZE))

print("AES CBC entropy: {}".format(count_entropy_of_text(encrypted)))

# print(count_entropy_of_text(t))

password_entropy = max_entropy_in_text(len(key), count_length_of_alphabet(key))

print("Entropy of password: {}".format(password_entropy))

if(password_entropy >= 100):
    if len(argv) > 3:
        f = open(argv[3], "wb")
    else:
        f = open("a", "xb")
    f.write(encrypted)
    f.close
    print("File encrypted")
else:
    print("Entropy of your password is too low!")