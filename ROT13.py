import fileinput

# ADVANTAGE: encrypting twice results in decryption

# macetrans maps characters from the first string to characters from the second: a->n, etc.
table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "nopqrstuvwxyzabcdefghijklm")

for line in fileinput.input():
    line = line.rstrip() 
    # rstrip deletes spaces (default setting)

    print(str.translate(line, table)) 
    # translate converts characters using the dictionary (here: table)
