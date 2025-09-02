class GeradorDeLog:

    def info(mensagem):
        return "[INFO]"
    
    def alerta(mensagem):
        return "[ALERT]"
    
    def erro(mensagem):
        return "[ERRO]"
    

mensagem = input("digite uma mensagem: ")

gerador_log1 = GeradorDeLog.info(mensagem)
gerador_log2 = GeradorDeLog.alerta(mensagem)
gerador_log3 = GeradorDeLog.erro(mensagem)

print(f"{gerador_log1} - {mensagem}")
print(f"{gerador_log2} - {mensagem}")
print(f"{gerador_log3} - {mensagem}")