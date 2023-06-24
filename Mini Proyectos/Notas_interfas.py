import tkinter as tk

def calcular_promedio():
    notas = []
    for i in range(1, 13):
        nota = float(entries[i-1].get())
        notas.append(nota)

    promedio = sum(notas) / len(notas)
    resultado_label.config(text="El promedio es: {:.2f}".format(promedio))

    if promedio >= 60:
        mensaje_label.config(text="Felicidades\n(⁠つ⁠✧⁠ω⁠✧⁠)⁠つ")

        if promedio > 65:
            mensaje2_label.config(text="Que pro")
        else:
            mensaje2_label.config(text="")
    else:
        mensaje_label.config(text="Te fue mal\nಠ⁠,⁠_⁠｣⁠ಠ")

        if promedio < 30:
            mensaje2_label.config(text="malísimo")
        else:
            mensaje2_label.config(text="")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de promedio")

# Crear etiquetas
labels = []
for i in range(1, 13):
    label = tk.Label(ventana, text="Nota {}: ".format(i))
    label.pack()
    labels.append(label)

# Crear campos de entrada
entries = []
for i in range(1, 13):
    entry = tk.Entry(ventana)
    entry.pack()
    entries.append(entry)

# Crear botón de cálculo
calcular_boton = tk.Button(ventana, text="Calcular", command=calcular_promedio)
calcular_boton.pack()

# Crear etiqueta de resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

# Crear etiquetas de mensajes
mensaje_label = tk.Label(ventana, text="")
mensaje_label.pack()
mensaje2_label = tk.Label(ventana, text="")
mensaje2_label.pack()

# Ejecutar la ventana principal
ventana.mainloop()