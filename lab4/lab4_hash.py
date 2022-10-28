import sys, string, crypt, random
from passlib.hash import sha256_crypt
import htpasswd

# htpasswd -> tym tworzymy baze, program prosi uzytk o haslo i sprawdza czy uzytkownik o takim hasle jest w bazie
# login : |...(hash)...|, htpasswd moze korzystac z roznych f hasz, mozemy wykorzystac crypt


if len(sys.argv) > 1:
    isValid = True
    passwd = sys.argv[1]
    f = open("/home/nebraszka/data-security-wut-22-/lab4/password", "r")
    for line in f:
        line = line.strip()
        line = line.split(":")
        salt = line[1][:2]
        encrypted = htpasswd.crypt(passwd, salt)
        if encrypted == line[1]:
            print("Haslo juz istnieje! Należy do użytkownika {}".format(line[0]))
            isValid = False
            break
    if isValid:
        print("Haslo poprawne")
else:
    print("Podaj hasło!")
    
    #zadanie 2 -> 



    