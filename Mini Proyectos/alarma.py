from time import localtime

H = input ("ingrese hora:")
M = input ("ingrese minuto:")

while True:
    if localtime ().tm_hour == int(H) and localtime().tm_min == int (M):
        print("Sonando alarma")