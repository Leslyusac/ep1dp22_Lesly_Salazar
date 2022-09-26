from Centro import Centro
class Publico(Centro):
    fecha_creacion= ""
    tipo = ""
    descripcion = ""

    def verDatosPublico(self):
        print("Fecha creación ", self.fecha_creacion, " Tipo: ", self.tipo, " Descripción: ", self.descripcion)
