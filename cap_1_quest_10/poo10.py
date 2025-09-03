class ConfiguracaoJogo:
    def __init__(self, resolucao_tela, volume_audio, dificuldade):
        self.resolucao_tela = resolucao_tela
        self.volume_audio = volume_audio
        self.deficuldade = dificuldade

configuracao_jogo1 = ConfiguracaoJogo("3840 x 2160", 1000, "Pandemônio")
configuracao_jogo2 = ConfiguracaoJogo("2560 x 1440", 10000, "Ultra-Pessadelo")

print("Resolução da Tela ",configuracao_jogo1.resolucao_tela,",", "Volume/Audio ",configuracao_jogo1.volume_audio,
      ",","Dificuldade" ,configuracao_jogo1.deficuldade )
print("Resolução da Tela ",configuracao_jogo2.resolucao_tela,",", "Volume/Audio ",configuracao_jogo2.volume_audio,
      ",","Dificuldade" ,configuracao_jogo2.deficuldade )
