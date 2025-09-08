import math # Importa a biblioteca 'math' para usar o valor de pi

class Circulo:
    def __init__(self, raio):
        """
        Inicializa o círculo com um raio.
        """
        self.raio = raio

    def calcular_area(self):
        """
        Calcula e retorna a área do círculo (A = pi * r^2).
        """
        area = math.pi * (self.raio ** 2)
        return area

    def calcular_circunferencia(self):
        """
        Calcula e retorna a circunferência do círculo (C = 2 * pi * r).
        """
        circunferencia = 2 * math.pi * self.raio
        return circunferencia

# --- Exemplo de uso da classe ---

# 1. Solicita ao usuário o raio do círculo
try:
    raio_do_circulo = float(input("Digite o raio do círculo de invocação: "))
    
    # 2. Cria uma instância da classe Circulo
    circulo_de_invocacao = Circulo(raio_do_circulo)

    # 3. Calcula e exibe a área e a circunferência
    area = circulo_de_invocacao.calcular_area()
    circunferencia = circulo_de_invocacao.calcular_circunferencia()
    
    print("-" * 35)
    print(f"Propriedades do Círculo Mágico:")
    print(f"Raio: {circulo_de_invocacao.raio:.2f}")
    print(f"Área de Invocação: {area:.2f}")
    print(f"Circunferência Mágica: {circunferencia:.2f}")
    print("-" * 35)

except ValueError:
    print("Entrada inválida. Por favor, digite um número para o raio.")