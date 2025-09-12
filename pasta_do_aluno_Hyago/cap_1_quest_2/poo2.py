
class FormatadorDeTexto:

    def para_caixa_alta(texto):
        return texto_digitado.upper()

    def para_caixa_baixa(texto):
        return texto_digitado.lower()
    
texto_digitado = input("Digite um texto: ")


formatar_texto1 = FormatadorDeTexto.para_caixa_alta(texto_digitado)
formatar_texto2 = FormatadorDeTexto.para_caixa_baixa(texto_digitado)

print(formatar_texto1)
print(formatar_texto2)