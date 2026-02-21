# utils.py
import os

def limpar_tela():
    # Detecta o SO e limpa o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho(idioma, dificuldade=None):
    print("\n" + "="*30)
    print(f"      JOGO DA FORCA - {idioma}")
    if dificuldade:
        print(f"      NÍVEL: {dificuldade}")
    print("="*30 + "\n")