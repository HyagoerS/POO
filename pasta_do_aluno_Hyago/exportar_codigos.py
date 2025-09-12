Pular para o conteúdo principal
Google Sala de Aula
Sala de Aula
2025.2 - POO - Programação Orientada a Objetos
Início
Agenda
Minhas inscrições
Pendentes
1
101695 - TEC.0434 - Programação para Web I - Graduação [67 h/80 Aulas]
1
102022 - TEC.1898 - Internet das Coisas - Graduação [33 h/40 Aulas]
1
101696 - TEC.0423 - Banco de Dados I - Graduação [67 h/80 Aulas]
2
2025.2 Fund. Redes de Computadores
TSI P3
2
2025.2 - POO - Programação Orientada a Objetos
9
95884 - TEC.0430 - Probabilidade e Estatística - Graduação [67 h/80 Aulas]
[
[TSI2025.1] Programação I - Programação Estruturada - Graduação
9
95888 - TEC.1399 - Gerenciamento de Projetos - Graduação [50 h/60 Aulas]
8
89250 - TEC.0044 - Inglês Instrumental - Graduação [50 h/60 Aulas]
8
89254 - TEC.1086 - Ética e Direitos Humanos - Graduação [33 h/40 Aulas]
2
2024.2 - Probabilidade e Estatística
8
89252 - TEC.0099 - Fundamentos da Metodologia Científica - Graduação [33 h/40 Aulas]
2
2024.1 Fundamentos da Matemática
8
82206 - TEC.1881 - Introdução à Programação Web - Graduação [67 h/80 Aulas]
8
82204 - TEC.1880 - Leitura e Produção Textual - Graduação [50 h/60 Aulas]
2
2024.1 Introdução à Informática
TSI P1
Turmas arquivadas
Configurações
Atividade 01 - Introdução
Atividade 01 - Introdução
Jales Anderson de Assis Monteiro
•
3 de set. (editado: 3 de set.)
100 pontos
Use o script em anexo para gerar as respostas das questões que devem ser colocadas no formulário da atividade, o documento anexo explica o funcionamento do script, basicamente ele vai gerar um .txt para cada questão (mesmo que a questão esteja dividida em vários arquivos e contenha subpastas), bastará copiar o conteúdo do arquivo gerado de cada questão e colocar no campo correspondente da questão no formulário.
Por segurança, verifique se o conteúdo do arquivo foi gerado corretamente antes de copiar e enviar.

exportar_codigos.py
Texto

Instruções: Como Exportar os Códigos de Todos os Seus Projetos
Documentos Google

Google Forms: Sign-in
https://docs.google.com/forms/d/e/1FAIpQLSdBRp82Nx-jIKV_bckjMZ6PujItcn-S6p8nRRta3Z6IjRg7EQ/viewform?usp=dialog
Comentários da turma
Seus trabalhos
Atribuído
Comentários particulares
import os
from pathlib import Path

def main():
    """
    Percorre todos os subdiretórios do diretório atual, tratando cada um
    como um projeto separado. Para cada projeto, consolida todos os
    arquivos .py em um único arquivo .txt nomeado após a pasta do projeto.
    """
    # Diretório raiz onde o script está sendo executado.
    student_root_dir = Path.cwd()
    
    # Obtém o nome do próprio script para ignorá-lo na busca.
    script_file = Path(__file__).name if '__file__' in globals() else 'user.py'
    
    print("Iniciando a consolidação de projetos...")
    
    # Itera sobre todos os itens no diretório raiz.
    for item in student_root_dir.iterdir():
        # Processa apenas se o item for um diretório (uma pasta de projeto).
        if item.is_dir():
            project_dir = item
            print(f"\nProcessando pasta: '{project_dir.name}'")
            
            # O arquivo de saída terá o nome da pasta do projeto e será salvo no diretório raiz.
            output_filename = student_root_dir / f"{project_dir.name}.txt"
            
            # Abre o arquivo .txt para escrita.
            with open(output_filename, 'w', encoding='utf-8') as outfile:
                # Usa os.walk para percorrer todos os arquivos dentro da pasta do projeto.
                for root, dirs, files in os.walk(project_dir):
                    # Remove a pasta '__pycache__' da busca para que não seja incluída.
                    if '__pycache__' in dirs:
                        dirs.remove('__pycache__')
                        
                    for file in files:
                        # Consolida apenas arquivos Python, ignorando o próprio script consolidador.
                        if file.endswith('.py') and file != script_file:
                            file_path = Path(root) / file
                            
                            # Calcula o caminho relativo ao diretório do projeto para manter a estrutura.
                            relative_path = file_path.relative_to(project_dir)
                            
                            # Escreve um cabeçalho de comentário para cada arquivo.
                            outfile.write('\n\n' + '#' * 80 + '\n')
                            outfile.write(f"# ARQUIVO: {relative_path}\n")
                            outfile.write('#' * 80 + '\n\n')
                            
                            # Escreve o conteúdo do arquivo .py no .txt.
                            try:
                                with open(file_path, 'r', encoding='utf-8') as infile:
                                    outfile.write(infile.read())
                            except Exception as e:
                                outfile.write(f"\n!!! Erro ao ler o arquivo: {e} !!!\n")

            print(f"-> Arquivo '{output_filename.name}' criado com sucesso.")
            
    print("\nConsolidação concluída!")

if __name__ == "__main__":
    main()

exportar_codigos.py
Exibindo exportar_codigos.py…