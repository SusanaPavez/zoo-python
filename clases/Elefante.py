from clases.animal import Animal


class Elefante(Animal):
    def __init__(self, nombre, edad, nivelsalud, felicidad):
        super().__init__(nombre, edad, nivelsalud, felicidad)
        super().alimentacion()
        self.alimentacion()
        self.nivelsalud = nivelsalud
        self.felicidad = felicidad

    def comer (self): #lo que le hace feliz, igual que a mí
        self.felicidad = +50
        print(
            f"El elefante {self.nombre} come, tiene un nivel de salud : {self.nivelsalud} y un nivel de felicidad {self.felicidad}"
        )
        return self


if __name__ == "__main__":
    try:
        elefante1 = Elefante("Fresia",29, 44, 33, 50)
        elefante1.display_info()
        elefante1.alimentacion()
        elefante1.display_info()
        elefante1.comer()
        elefante1.display_info()

    except Exception as err:
        print("Error", err)
        print("Hay un error en la clase Elefante")
