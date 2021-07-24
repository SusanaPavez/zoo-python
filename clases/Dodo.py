from clases.animal import Animal

class Dodo(Animal):
    def __init__(self, nombre,edad,nivelsalud,felicidad):
        super().__init__(nombre,edad,nivelsalud,felicidad)
        super().alimentacion()
        self.alimentacion()
        self.nivelsalud = nivelsalud
        self.felicidad = felicidad
        


    def dodea(self): # actividad quehace feliz al dodo
        self.felicidad =+50
        print(f"El dodo {self.nombre} dodea,tiene un nivel de salud : {self.nivelsalud} y un nivel de felicidad {self.felicidad}")
        return self

if __name__ == "__main__":
    try:
        dodo1 = Dodo("Dodito", 22, 33, 44, 55)
        dodo1.display_info()
        dodo1.alimentacion()
        dodo1.display_info()
        dodo1.dodea()
        dodo1.display_info()

    except Exception as err:
        print("Error", err)
        print("Hay un error en la clase Dodo")
