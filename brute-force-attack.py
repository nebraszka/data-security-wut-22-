from entropy import count_entropy_of_text
from sys import argv
from Crypto.Cipher import ARC4

if len(argv) != 2:
    exit()

#number_of_decryptions = int(argv[2])

file = open(argv[1], "rb")  # encrypted text
text = file.read()

# 3 digit key
min_entropy = 10000
ARC4.key_size = range(3, 257)

for i in range(97, 123):
    for j in range(97, 123):
        for k in range(97, 123):
            key = chr(i) + chr(j) + chr(k)
            arc = ARC4.new(str.encode(key))
            decrypted = arc.decrypt(text)
            # TODO: with for it's not working
            # decrypted = arc.decrypt(decrypted)
            # decrypted = arc.decrypt(decrypted)
            entropy = count_entropy_of_text(
                decrypted)
            if entropy < min_entropy:
                min_entropy_key = key
                min_entropy = entropy
                decrypted_text = decrypted.decode('latin-1', 'ignore')

print("Key found! It's: {}\nEntropy is: {}\nDecrypted text:\n{}".format(
    min_entropy_key, min_entropy, decrypted_text))
