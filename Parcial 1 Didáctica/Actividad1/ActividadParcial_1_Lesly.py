import tkinter
ventana = tkinter.Tk()
ventana.geometry("500x600")
ventana.title("Calculo de valores")
suma=0.0
producto =0.0
resultado=0.0

def promedio():
    resultado=float(txt_valor1.get())+float(txt_valor2.get())+float(txt_valor3.get())+float(txt_valor4.get())+float(txt_valor5.get())
    suma = resultado
    resultado=resultado/5
    lbl_resultado["text"]=resultado

def mayor():
    if txt_valor1.get() > txt_valor2.get() and txt_valor1.get() > txt_valor3.get() and txt_valor1.get() > txt_valor4.get() and txt_valor1.get() > txt_valor5.get():
        lbl_mayor["text"]= 'El numero mayor es: ',txt_valor1.get()
    #dos
    elif txt_valor2.get() > txt_valor1.get() and txt_valor2.get() > txt_valor3.get() and txt_valor2.get() > txt_valor4.get() and txt_valor2.get() > txt_valor5.get():
        lbl_mayor["text"]= 'El numero mayor es: ',txt_valor2.get()
    #tres
    elif txt_valor3.get() > txt_valor1.get() and txt_valor3.get() > txt_valor2.get() and txt_valor3.get() > txt_valor4.get() and txt_valor3.get() > txt_valor5.get():
        lbl_mayor["text"]= 'El numero mayor es: ',txt_valor3.get()
    #cuatro
    elif txt_valor4.get() > txt_valor1.get() and txt_valor4.get() > txt_valor2.get() and txt_valor4.get() > txt_valor3.get() and txt_valor4.get() > txt_valor5.get():
        lbl_mayor["text"]= 'El numero mayor es: ',txt_valor4.get()
    #cinco
    elif txt_valor5.get() > txt_valor1.get() and txt_valor5.get() > txt_valor2.get() and txt_valor5.get() > txt_valor3.get() and txt_valor5.get() > txt_valor4.get():
        lbl_mayor["text"]= 'El numero mayor es: ',txt_valor5.get()
    
def comparacion():
    producto = float(txt_valor1.get()) * float(txt_valor5.get())
    if suma > producto:
        lbl_sumaMultiplo["text"] ="Es mayor la suma"
    elif suma == producto:
        lbl_sumaMultiplo["text"] ="La suma y el producto son iguales"
    else:
        lbl_sumaMultiplo["text"]= "La suma es menor al producto"

lbl_titulo=tkinter.Label(ventana, text="Calcular promedio", bg="yellow", font=("Calibri",16))
lbl_titulo.pack(fill=tkinter.X, pady=8)

lbl_valor1=tkinter.Label(ventana, text="Ingrese el primer valor", bg="green", font=("Calibri",14))
lbl_valor1.pack()

txt_valor1=tkinter.Entry(ventana,bg="pink", font="Calibri")
txt_valor1.pack(fill=tkinter.X, pady=8)

lbl_valor2=tkinter.Label(ventana, text="Ingrese el segundo valor", bg="green", font=("Calibri",14))
lbl_valor2.pack()
txt_valor2=tkinter.Entry(ventana,bg="pink", font="Calibri")
txt_valor2.pack(fill=tkinter.X, pady=8)

lbl_valor3=tkinter.Label(ventana, text="Ingrese el tercer valor", bg="green", font=("Calibri",14))
lbl_valor3.pack()
txt_valor3=tkinter.Entry(ventana,bg="pink", font="Calibri")
txt_valor3.pack(fill=tkinter.X, pady=8)

lbl_valor4=tkinter.Label(ventana, text="Ingrese el cuarto valor", bg="green", font=("Calibri",14))
lbl_valor4.pack()
txt_valor4=tkinter.Entry(ventana,bg="pink", font="Calibri")
txt_valor4.pack(fill=tkinter.X, pady=8)

lbl_valor5=tkinter.Label(ventana, text="Ingrese el quinto valor", bg="green", font=("Calibri",14))
lbl_valor5.pack()
txt_valor5=tkinter.Entry(ventana,bg="pink", font="Calibri")
txt_valor5.pack(fill=tkinter.X, pady=8)

btn_promedio = tkinter.Button(ventana, text="Calcular promedio", command=promedio)
btn_promedio.pack(fill=tkinter.X, pady=8)

btn_mayor = tkinter.Button(ventana, text="El mayor es: ", command=mayor)
btn_mayor.pack(fill=tkinter.X, pady=8)

btn_sumaMultiplo = tkinter.Button(ventana, text="Comparar la suma y el múltiplo: ", command=comparacion)
btn_sumaMultiplo.pack(fill=tkinter.X, pady=8)


lbl_resultado=tkinter.Label(ventana, text="Resultado")
lbl_resultado.pack(fill=tkinter.X)


lbl_mayor=tkinter.Label(ventana, text="Mayor es")
lbl_mayor.pack(fill=tkinter.X)


lbl_sumaMultiplo=tkinter.Label(ventana, text="La suma es Mayor Igual o Menor que el Múltiplo")
lbl_sumaMultiplo.pack(fill=tkinter.X)



ventana.mainloop()  