
import tkinter as tk
import random

pila = []

colores = ["red", "blue", "green", "yellow", "orange", "pink", "purple", "cyan"]

def mostrar_pila():
    lienzo.delete("all")

    lienzo.create_text(
        200, 20,
        text="TOPE DE LA PILA",
        font=("Arial", 12, "bold")
    )

    if not pila:
        lienzo.create_text(
            200, 150,
            text="Pila vacia",
            font=("Arial", 14)
        )
    else:
        for i, elemento in enumerate(reversed(pila)):
            x1 = 100
            y1 = 45 + i * 45
            x2 = 300
            y2 = y1 + 40

            lienzo.create_rectangle(
                x1, y1, x2, y2,
                fill=elemento["color"],
                outline="black"
            )

            lienzo.create_text(
                200, y1 + 20,
                text=elemento["valor"],
                font=("Arial", 14)
            )

    lienzo.configure(
        scrollregion=(0, 0, 400, max(300, 60 + len(pila) * 45))
    )

    contador.config(
        text="Elementos en la pila: " + str(len(pila))
    )

def apilar():
    valor = entrada.get().strip()

    if valor:
        color = random.choice(colores)

        pila.append({
            "valor": valor,
            "color": color
        })

        entrada.delete(0, tk.END)
        mostrar_pila()
        mensaje.config(text="Elemento apilado: " + valor)
    else:
        mensaje.config(text="Escribe un elemento primero")

def ver_cima():
    if pila:
        mensaje.config(text="La cima es: " + pila[-1]["valor"])
    else:
        mensaje.config(text="La pila esta vacia")

def desapilar():
    if pila:
        elemento = pila.pop()
        mostrar_pila()
        mensaje.config(text="Se desapilo: " + elemento["valor"])
    else:
        mensaje.config(text="La pila esta vacia")

def vaciar_pila():
    pila.clear()
    mostrar_pila()
    mensaje.config(text="La pila ha sido vaciada")

ventana = tk.Tk()
ventana.title("Pila - Estructura de Datos")
ventana.geometry("450x600")
ventana.resizable(False, False)

titulo = tk.Label(
    ventana,
    text="PILA",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=8)

entrada = tk.Entry(
    ventana,
    font=("Arial", 14),
    justify="center"
)
entrada.pack(pady=4)

entrada.bind("<Return>", lambda evento: apilar())

boton_apilar = tk.Button(
    ventana,
    text="Apilar",
    command=apilar,
    width=18
)
boton_apilar.pack(pady=3)

boton_cima = tk.Button(
    ventana,
    text="Ver cima",
    command=ver_cima,
    width=18
)
boton_cima.pack(pady=3)

boton_desapilar = tk.Button(
    ventana,
    text="Desapilar",
    command=desapilar,
    width=18
)
boton_desapilar.pack(pady=3)

boton_vaciar = tk.Button(
    ventana,
    text="Vaciar pila",
    command=vaciar_pila,
    width=18
)
boton_vaciar.pack(pady=3)

marco = tk.Frame(ventana)
marco.pack(pady=5)

barra = tk.Scrollbar(
    marco,
    orient=tk.VERTICAL
)
barra.pack(side=tk.RIGHT, fill=tk.Y)

lienzo = tk.Canvas(
    marco,
    width=400,
    height=230,
    bg="white",
    yscrollcommand=barra.set
)
lienzo.pack(side=tk.LEFT)

barra.config(command=lienzo.yview)

contador = tk.Label(
    ventana,
    text="Elementos en la pila: 0",
    font=("Arial", 10)
)
contador.pack(pady=3)

mensaje = tk.Label(
    ventana,
    text="Pila vacia",
    font=("Arial", 10)
)
mensaje.pack(pady=3)

mostrar_pila()

ventana.mainloop()
