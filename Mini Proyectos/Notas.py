


cantidad = int (input("Ingrese cantidad a calcular : "))
notas = []

#bucle para ingresar notas
for i in range (1, cantidad + 1):
    nota = float (input("Notas {} : ".format(i)))
    notas.append(nota)

#Resultado del promedio
promedio = sum(notas) / len(notas)
print ("El promedio es: ", promedio)


#algunos mensajitos
if  promedio >= 60 :
    print ("Felicidades")
    print ("(⁠つ⁠✧⁠ω⁠✧⁠)⁠つ")
    
    if promedio > 65 :
        print ("Que pro")
    
else :
    print ("Te fue mal")
    print ("ಠ⁠,⁠_⁠｣⁠ಠ")
       
    if promedio < 30:
        print ("malísimo")


