# from Elefante import Elefante
# from Dodo import Dodo
# from Ornitorrinco import Ornitorrinco


print(f"Bienvenido a Jurasic Park")
listaZoo=[]
while True:
    print(f"\nOpciones")
    print(f"Selecciona una opcion:  \n1.Crear Zoo  \n2.Registrar Dodo  \n3.Registrar Ornitorrinco \n4.Registrar Elefante\n5.Mostrar animales \n0.Salir")
    n = int(input("Escoge: "))
    
    if n == 1:
        nombre = input("\nNombre del Zoo: ")
        zoo = zoo(nombre)
        print("\n Se ha creado el zoo ", nombre)
        listaZoo.append(zoo)

    if n == 2:
        nombre = input("\nNombre del Dodo: ")
        edad = int(input("Edad: "))
        peso = int(input("Peso: "))
        Dodo = Dodo(0, nombre, edad, 0, 0, peso)
        Dodo.dodear()
        Dodo.display_info()
        nombre_zoo = input("Ingresa el nombre del zoologico para el animal: ")
        for zoologico in listaZoo:
            if zoologico.nombre == nombre_zoo:
                zoologico.add_Dodo(Dodo)
                zoologico.print_all_info()
            else:
                print("No se encontró el zoologico con ese nombre")

    if n == 3:
        nombre = input("\nNombre del Ornitorrinco: ")
        edad = int(input("Edad: "))
        peso = int(input("Peso: "))
        Ornitorrinco = Ornitorrinco(0, nombre, edad, 0, 0, peso)
        Ornitorrinco.graznar()
        Ornitorrinco.display_info()
        nombre_zoo = input("Ingresa el nombre del zoologico para el animal: ")
        for zoologico in listaZoo:
            if zoologico.nombre == nombre_zoo:
                zoologico.add_Ornitorrinco(Ornitorrinco)
                zoologico.print_all_info()
            else:
                print("No se encontró el zoologico con ese nombre")

    if n == 4:
        nombre = input("\nNombre del Elefante: ")
        edad = int(input("Edad: "))
        peso = int(input("Peso: "))
        Elefante = Elefante(0, nombre, edad, 0, 0, peso)
        Elefante.comer()
        Elefante.display_info()
        nombre_zoo = input("Ingresa el nombre del zoologico para el animal: ")
        for zoologico in listaZoo:
            if zoologico.nombre == nombre_zoo:
                zoologico.add_Elefante(Elefante)
                zoologico.print_all_info()
            else:
                print("No se encontró el zoologico con ese nombre")

    if n == 5:
        nombre_zoo = input("Ingresa el nombre del zoologico para ver los animales: ")
        for zoologico in listaZoo:
            if zoologico.nombre == nombre_zoo:
                zoologico.print_all_info()
            else:
                print("No se encontró el zoologico con ese nombre")

    if n == 0 :
        print("Hasta luego")
        break

