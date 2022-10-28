from passlib.hash import sha256_crypt

hash = sha256_crypt.hash("password")
print(hash) # wypisanie wartości funkcji skrótu

check = sha256_crypt.verify("password", "$5$rounds=535000$Y6FjDW3EKlAPYTQ8$l.jd1WloelVKsV0PDHlH45.j.L2SB3rQkhrYPeWMu87")
print(check) # wypisanie informacji czy hasło "password" odpowiada podanemu wyżej skrótowi