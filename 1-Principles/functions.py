def saludar ():
    print("¡¡Buenos días!!")
    
saludar()

def saludarA(name="Julio"):
    print("¡Buenos días, {}!".format(name))
    
saludarA()
saludarA("Mario")

def despedir(name, causa):
    print("{name}, has sido despedido por {causa}, no vengas mañana"
          .format(name=name, causa=causa))

despedir("Manolo", "Robar pan de miga de la cafetería")
despedir("Juan Carlos de los Corazones de Jesús, José y María", "tener un nombre muy largo para la lista diaria")


def usandoFStrings(arg):
    print(f"Estoy solo quiero decir que {arg}")
    
usandoFStrings("me gustan las batatas")