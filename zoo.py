from clases.Elefante import Elefante
from clases.Dodo import Dodo
from clases.Ornitorrinco import Ornitorrinco

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_elefante(self,animal):
        self.animals.append(animal)
    def add_dodo(self,animal):
        self.animals.append(animal)
    def add_ornitorrinco(self,animal):
        self.animals.append(animal)
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()


Elefante1 = Elefante( "Fresia",25, 10, 30)
Elefante1.display_info()
Dodo1 = Dodo("Perry",7, 28, 33)
Dodo1.display_info()
Ornitorrinco1 = Ornitorrinco("Perry", 48, 23, 43 )
Ornitorrinco1.display_info()

zoo1 = Zoo("No es Jurasic Park")
zoo1.add_Elefante(Elefante1) 
zoo1.add_dodo(Dodo1)
zoo1.add_ornitorrinco(Ornitorrinco1)
zoo1.print_all_info()

zoo2 = Zoo("Tampoco es Jurasic Park")
zoo2.add_Elefante(Elefante1) 
zoo2.add_Dodo(Dodo1)
zoo2.add_Ornitorrinco(Ornitorrinco1)
zoo2.print_all_info()

for animal in zoo1.animals: 
    animal.alimentacion()
#clase.metodo.variable(objeto)


