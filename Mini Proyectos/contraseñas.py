import random

minus = "abcdefghijklmnñopqrstvwxyz"
mayus = minus.upper()
num = "1234567890"
simb = "@()[]+-?¡¿$#!" 

base = minus + mayus + num + simb
longitud = 12

for _ in range(10):
    muestra = random.sample(base,longitud)
    password = "".join(muestra)
    print(password)

