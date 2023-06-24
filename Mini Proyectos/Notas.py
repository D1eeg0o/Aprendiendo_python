
notas = []
for i in range (1, 13):
    nota = float (input("Notas {} : ".format(i)))
    notas.append(nota)

promedio = sum(notas) / len(notas)
print ("El promedio es: ", promedio)

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