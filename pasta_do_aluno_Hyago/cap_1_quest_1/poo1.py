import math
class CalculadoraGeometrica:

    def calcular_area_quadrado(lado):
        return  lado ** 2

    def calcular_area_circulo(raio):
        return 3.1415 * raio ** 2
    
raio = int(input("Digite o raio: "))
lado = int(input("Digite o lado: "))

area_quadrado = CalculadoraGeometrica.calcular_area_quadrado(raio)
area_circulor = CalculadoraGeometrica.calcular_area_circulo(raio)

print(area_quadrado)
print(area_circulor)
