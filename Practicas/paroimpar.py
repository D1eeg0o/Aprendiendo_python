
#primera vercion
numero = int (input("ingrese numero: "))

if numero & 1==0:                            #aqui esta usando el operador de bits
    print("Tu numero es par")

else:
    print("Tu numero es inpar")



#sugerencia a mejora
numero = int (input("Ingrese numero: "))

if numero % 2 == 0:                           #aqui cambia al operador modulo
    print("tu numero en par")

else:
    print("tu numero es inpar")