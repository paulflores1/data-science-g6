#programacion orientada a objetos

class Automovil:
    def __init__(self,aa,pl,col,mar):
        self.ano_auto=aa
        self.placa=pl
        self.color=col
        self.marca=mar
    def encender(self):
        print(f"El automovil {self.marca} ha sido encendido")
    def avanzar(self):
        print(f"El automovil {self.marca} esta avanzando")
    def acelerar(self):
        print(f"El automovil {self.marca} esta acelerando")
    def frenar(self):
        print(f"El automovil {self.marca} esta frenando")


wolsgwagen=Automovil(2020,"ABC123","Rojo","Wolkswagen")
wolsgwagen.encender()
wolsgwagen.avanzar()    
wolsgwagen.acelerar()
wolsgwagen.frenar()

tico=Automovil(2015,"XYZ789","Azul","tico")
tico.encender()
tico.avanzar()
tico.acelerar()
tico.frenar()