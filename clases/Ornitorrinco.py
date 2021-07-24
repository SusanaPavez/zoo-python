from clases.animal import Animal


class Ornitorrinco(Animal): #por qué se me ocurrió un nombre tan largo?
    def __init__(self, nombre,edad,nivelsalud,felicidad):
        super().__init__(nombre,edad,nivelsalud,felicidad)
        super().alimentacion()
        self.alimentacion()
        self.nivelsalud = nivelsalud
        self.felicidad = felicidad


#que actividad le produce felicidad al loro
    def grazna(self):
        self.felicidad =+50
        print(f"El ornitorrinco {self.nombre} grazna,tiene un nivel de salud : {self.nivelsalud} y un nivel de felicidad {self.felicidad}")
        return self

if __name__ == '__main__':
    try:
        ornitorrico1 = Ornitorrinco( "Perry", 22, 33, 44, 55 )
        ornitorrico1.display_info()
        ornitorrico1.alimentacion()
        ornitorrico1.display_info()
        ornitorrico1.cacarear()
        ornitorrico1.display_info()
        
    except Exception as err:
        print("Error", err)
        print("Hay un error en la clase Ornitorrinco")
