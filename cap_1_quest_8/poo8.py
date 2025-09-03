class Ponto2D:
    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY

coordenadas = Ponto2D(150, 150)
print(coordenadas.coordX, ",", coordenadas.coordY)