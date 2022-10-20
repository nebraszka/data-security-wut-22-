from sys import argv, stdout
from Crypto.Cipher import ARC4

if len(argv) != 4:
    print("How to run this program:\n" + argv[0] + 
    " <key> <how long keystream> <keystream mode>\n" + 
    "Keystream modes:\n1 - chars\n2 - integers")
    exit()

mode = int(argv[3])
if mode not in [1,2]:
    print("Wrong mode!\nHow to run this program:\n" + 
    argv[0] + " "                                   + 
    "<key> <how long keystream> <keystream mode>\n" + 
    "Keystream modes:\n1 - chars\n2 - integers")
    exit()

def swap(s, i, j):
    tmp = s[i]
    s[i] = s[j]
    s[j] = tmp

s = []

for i in range(0, 256):
    s.append(i)

key = list(argv[1])

j = 0
for i in range (0, 256):
    j = (j + s[i] + ord(key[i % len(key)])) % 256
    swap(s, i, j)

i = 0
j = 0

keystream = ""

for k in range(0, int(argv[2])):
    i = (i + 1) % 256
    j = (j + s[i]) % 256
    swap(s, i, j)
    keystream += chr(s[(s[i] + s[j]) % 256])

if mode == 1:
    print(keystream)
else:
    for char in keystream:
        stdout.write(str(ord(char)) + " ")