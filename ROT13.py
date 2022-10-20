import fileinput

# maketrans mapuje chary z pierwszego stringa na chary z drugiego a->n itp.
table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "nopqrstuvwxyzabcdefghijklm")

for line in fileinput.input():
    line = line.rstrip() 
    # rstrip usuwa spacje defaultowo

    print(str.translate(line, table)) 
    # translate zamienia znaki korzystajac ze slownika (tu: table)
