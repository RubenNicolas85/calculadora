#Crearemos una calculadora gráfica con Tkinter que te permitirá una interfaz visual
#más amigable para el usuario. A continuación se muestra cómo hacerla: 

import tkinter as tk

#Función para agregar el número u operador al campo de entrada
def agregar_numero(numero):
    entrada.insert(tk.END, numero)

#Funciones para realizar las operaciones aritméticas básicas(+ - * /):
def realizar_operacion():
    try:
        resultado = eval(entrada.get()) #Evalúa la expresión matemática ingresada 
        entrada.delete(0,tk.END) #Borra el contenido del campo de entrada
        entrada.insert(tk.END,str(resultado)) #Muestra el resultado en el campo de entrada
    except Exception as e:
        entrada.delete(0,tk.END)
        entrada.insert(tk.END, "Error")

#Función para limpiar el campo de entrada:
def limpiar():
    entrada.delete(0,tk.END)

#Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

#Creamos el campo de entrada: 
entrada = tk.Entry(ventana, font=("Arial", 20), justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Lista de botones con sus respectivos valores y la ubicación en la cuadrícula: 
botones = [
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3), 
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3), 
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3), 
    ("0",4,0),(".",4,1),("=",4,2),("+",4,3), 
]

#Creamos los botones y los ubicamos en la cuadrícula: 
for valor, fila, columna in botones:
    boton = tk.Button(ventana,text=valor,font=("Arial",20),command=lambda v=valor:
    agregar_numero(v))
    
    boton.grid(row=fila, column=columna, padx=5, pady=6,sticky="nsew")

#Creamos el botón para limpiar el campo de entrada: 
limpiar_boton = tk.Button(ventana,text="C", font=("Arial",20), command=limpiar)
limpiar_boton.grid(row=5, column=0,padx=5,pady=5,columnspan=2,sticky="nsew")

#Creamos el botón de igual para obtener el resultado: 
calcular_boton = tk.Button(ventana,text="=", font=("Arial",20), command=realizar_operacion)
calcular_boton.grid(row=5,column=2,padx=5,pady=5,columnspan=2, sticky="nsew")

#Iniciamos el bucle principal de la aplicación: 
ventana.mainloop()



