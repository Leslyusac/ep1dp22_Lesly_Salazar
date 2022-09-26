from Publico import Publico
class Mixto(Publico):
    cantidad_hombres=0
    cantidad_mujeres=0

    def verDatosMixto(self):
        print("Cantidad hombres: ", self.cantidad_hombres, " Cantidad mujeres: ", self.cantidad_mujeres)
