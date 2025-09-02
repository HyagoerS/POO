class ConversorSimples:

    def real_para_dolar(valor_real):
        return valor_real // 5.25
    
    def dolar_para_real(valor_dolar):
        return valor_dolar * 5.25

receber = int(input("Digite a quantia a sacar: "))

real = ConversorSimples.real_para_dolar(receber)
dolar = ConversorSimples.dolar_para_real(receber)

print(real)
print(dolar)

