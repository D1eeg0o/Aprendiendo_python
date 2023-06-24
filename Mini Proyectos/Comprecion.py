lista = ["dado", "solo", "yuy"]
nueva = []
for x in lista :
    if "o" in x:
        nueva.append(x)
print (nueva)



lista = ["dado", "solo", "yuy"]
nueva = [x for x in lista if "o" in x]
print(nueva)



frutas = ["manzana", "platano", "kiwi", "durazno"]
new = [x for x in frutas if x != "kiwi"] 
print(new)


