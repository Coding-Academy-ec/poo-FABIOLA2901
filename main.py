import math
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
       return self.base* self.altura

        #pass # implementación de la función con la forula de área de un rectángulo
base = float(input("Ingrese la base de Rectangulo : "))
altura = float(input("Ingrese la altura Rectangulo : "))
rectangulo1 = Rectangulo(base, altura)
print(f"Al area del Rectangulo es: {  rectangulo1.area()}")
  

class Circulo:
    #pi = 3.141592653589793

    def __init__(self, radio):
        #pass # inicialización de la variable radio
        self.radio = radio

    def areacirculo(self):
         # implementación de la función con la forula de área de un círculo
         return math.pi * (self.radio ** 2)
    
radio = float(input("Ingrese el radio de la circulo: "))
Circulo1=Circulo(radio)
print(f"Al area de la circulo es: {  Circulo1.areacirculo()}.2f")