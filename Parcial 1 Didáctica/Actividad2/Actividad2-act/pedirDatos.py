from Mixto import Mixto
import tkinter
from tkinter import *
from tkinter import ttk


#Creación de ventana
ventana = tkinter.Tk()
ventana.title = "Centro Educativo"
ventana.geometry("1100x900")
resultado=0.0


#Tabla
tabla = ttk.Treeview(ventana,columns=("cnombre","cdireccion","ctelefono","cdirector","curl", "c_fecha","ctipo","cdescripcion","chombres","cmujeres"))


listaCentro = []

def cargarDatos():
    informacion2 = Mixto()
    informacion2.codigo = int(txt_valor1.get())
    informacion2.nombre = txt_valor2.get()
    informacion2.direccion = txt_valor3.get()
    informacion2.telefono = txt_valor4.get()
    informacion2.director = txt_valor5.get()
    informacion2.url = txt_valor6.get()
    informacion2.fecha_creacion = txt_valor7.get()
    informacion2.tipo = txt_valor8.get()
    informacion2.descripcion = txt_valor9.get()
    informacion2.cantidad_hombres = txt_valor10.get()
    informacion2.cantidad_mujeres = txt_valor11.get()



    listaCentro.append(informacion2)
    generarTabla()
    
def generarTabla():
    for fila in tabla.get_children():
        tabla.delete(fila)

    #tamaño de columnas
    tabla.column("#0",width=10)
    #tabla.column("ccod", width=30)
    tabla.column("cnombre", width=30)
    tabla.column("cdireccion",width=30)
    tabla.column("ctelefono" , width=30)
    tabla.column("cdirector", width=30)
    tabla.column("curl", width=30)
    tabla.column("c_fecha", width=30)
    tabla.column("ctipo", width=30)
    tabla.column("cdescripcion", width=30)
    tabla.column("chombres", width=30)
    tabla.column("cmujeres", width=30)
    

    tabla.heading("#0", text="Codigo Centro",anchor=CENTER)
    #tabla.heading("ccod", text="Codigo", anchor=CENTER)
    tabla.heading("cnombre", text="Nombre", anchor=CENTER)
    tabla.heading("cdireccion", text= "Direccion", anchor=CENTER)
    tabla.heading("ctelefono", text= "Telefono", anchor=CENTER)
    tabla.heading("cdirector", text= "Director", anchor=CENTER)
    tabla.heading("curl", text= "URL", anchor=CENTER)
    tabla.heading("c_fecha", text= "Fecha", anchor=CENTER)
    tabla.heading("ctipo", text= "Tipo", anchor=CENTER)
    tabla.heading("cdescripcion", text= "Descripcion", anchor=CENTER)
    tabla.heading("chombres", text= "Cant Hombres", anchor=CENTER)
    tabla.heading("cmujeres", text= "Cant Mujeres", anchor=CENTER)


#Carga a la tabla
    for registros in listaCentro:
        
        tabla.insert("",END, text=registros.codigo, values=(registros.nombre, registros.direccion, registros.telefono, registros.director, registros.url, registros.fecha_creacion, registros.tipo, registros.descripcion, registros.cantidad_hombres, registros.cantidad_mujeres ) )
    
    tabla.pack(fill= tkinter.X)

    

#creación de elementos de ventana


def almacenar(sef):
    print ("Se estan guardando los datos")


lbl_titulo=tkinter.Label(ventana, text="Formulario de registro centro educativo", bg="yellow", font=("Calibri",12))
lbl_titulo.pack(fill=tkinter.X, pady=8)


lbl_valor1=tkinter.Label(ventana, text="Codigo centro", bg="green", font=("Calibri",10))
lbl_valor1.pack()
txt_valor1=tkinter.Entry(ventana,bg="pink", font=("Calibri",10))
txt_valor1.pack(fill=tkinter.X, pady=2)


lbl_valor2=tkinter.Label(ventana, text="Nombre centro", bg="green", font=("Calibri",10))
lbl_valor2.pack()
txt_valor2=tkinter.Entry(ventana,bg="pink", font=("Calibri",10))
txt_valor2.pack(fill=tkinter.X, pady=2)

lbl_valor3=tkinter.Label(ventana, text="Dirección centro", bg="green", font=("Calibri",10))
lbl_valor3.pack()
txt_valor3=tkinter.Entry(ventana,bg="pink", font=("Calibri",10))
txt_valor3.pack(fill=tkinter.X, pady=2)


lbl_valor4=tkinter.Label(ventana, text="Teléfono centro", bg="green", font=("Calibri",10))
lbl_valor4.pack()
txt_valor4=tkinter.Entry(ventana,bg="pink", font=("Calibri",10))
txt_valor4.pack(fill=tkinter.X, pady=2)


lbl_valor5=tkinter.Label(ventana, text="Director centro", bg="green", font=("Calibri",10))
lbl_valor5.pack()
txt_valor5=tkinter.Entry(ventana,bg="pink", font=("Calibri",10))
txt_valor5.pack(fill=tkinter.X, pady=2)


lbl_valor6=tkinter.Label(ventana, text="Url centro", bg="green", font=("Calibri",10))
lbl_valor6.pack()
txt_valor6=tkinter.Entry(ventana,bg="pink", font=("Calibri",10))
txt_valor6.pack(fill=tkinter.X, pady=2)



lbl_valor7=tkinter.Label(ventana, text="Fecha creación", bg="green", font=("Calibri",10))
lbl_valor7.pack()
txt_valor7=tkinter.Entry(ventana,bg="pink", font=("Calibri",10))
txt_valor7.pack(fill=tkinter.X, pady=2)



lbl_valor8=tkinter.Label(ventana, text="Tipo centro", bg="green", font=("Calibri",10))
lbl_valor8.pack()
txt_valor8=tkinter.Entry(ventana,bg="pink", font=("Calibri",10))
txt_valor8.pack(fill=tkinter.X, pady=2)


lbl_valor9=tkinter.Label(ventana, text="Descripción centro", bg="green", font=("Calibri",10))
lbl_valor9.pack()
txt_valor9=tkinter.Entry(ventana,bg="pink", font=("Calibri",10))
txt_valor9.pack(fill=tkinter.X, pady=2)


lbl_valor10=tkinter.Label(ventana, text="Cantidad Hombres", bg="green", font=("Calibri",10))
lbl_valor10.pack()
txt_valor10=tkinter.Entry(ventana,bg="pink", font=("Calibri",10))
txt_valor10.pack(fill=tkinter.X, pady=2)


lbl_valor11=tkinter.Label(ventana, text="Cantidad Mujeres", bg="green", font=("Calibri",10))
lbl_valor11.pack()
txt_valor11=tkinter.Entry(ventana,bg="pink", font=("Calibri",10))
txt_valor11.pack(fill=tkinter.X, pady=2)


btn_promedio = tkinter.Button(ventana, text="Cargar los datos", command=cargarDatos)
btn_promedio.pack(fill=tkinter.X, pady=2)



ventana.mainloop()


#creo la instancia 
#informacion = Mixto()

#informacion.codigo=10
#informacion.nombre="Centro Regional1"
#informacion.direccion="Zona 4"
#informacion.telefono ="441152"
#informacion.director ="Juan Jose Pacheco"
#informacion.url ="http://centroRegional1.com"
#informacion.fecha_creacion="15-03-1985"
#informacion.tipo = "Multicultural"
#informacion.descripcion ="Centro para jovenes de region norte"
#informacion.cantidad_hombres=50
#informacion.cantidad_mujeres=15



#informacion.verDatosCentro()
#informacion.verDatosPublico()
#informacion.verDatosMixto()