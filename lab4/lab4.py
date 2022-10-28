import sys
import crypt
import string
import random

password = sys.argv[1]

salt = ''.join(random.sample(string.ascii_letters, 2))

protected_password = crypt.crypt(password, salt)
print( protected_password )

