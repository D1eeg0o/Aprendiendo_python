lista = ["zalas", "xenon", "auto", "hola"]
lista.sort()
print(lista)


listanum = [100, 9, 594, 540, 953]
listanum.sort()
resultado = sum(listanum)
print(listanum, resultado)

if resultado >500:
    print("alto")

else :
        print ("bajo")





fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
