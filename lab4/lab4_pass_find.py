import sys, string, crypt

passwd = sys.argv[1]
chars = string.ascii_letters
for a in chars:
    for b in chars:
        for c in chars:
            trial = a+b+c
            crypted = crypt.crypt(trial, passwd)
            if crypted == passwd:
                break
        if crypted == passwd:
            break
    if crypted == passwd:
        break

if crypted == passwd:
    print( "Hasło złamane: " + trial)  
else:
    print( "Nie złamano hasła" )