class GeradorDeLog:

    def info(mensagem):
        return
    
    def alerta(mensagem):
        return 
    
    def erro(mensagem):
        return
mensagem = input("digite uma mensagem: ")

gerador1 = GeradorDeLog.info(mensagem)
gerador2 = GeradorDeLog.alerta(mensagem)
gerador3 = GeradorDeLog.erro(mensagem)

print(gerador1)
print(gerador2)
print(gerador3)