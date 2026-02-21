# main.py

# 1. Importamos as nossas peças (módulos)
import constantes
import utils
import api_engine
import random

def novo_jogo():
    utils.limpar_tela()
    print("Bem-vindo ao Jogo da Forca 2.0!")
    
    # 2. Seleção de Idioma
    print("\nEscolha o idioma / Choose language:")
    print("1. Português (PT)")
    print("2. English (EN)")
    print("3. 日本語 (JP)")
    
    opcao = input("\nOpção: ")
    idiomas = {"1": "PT", "2": "EN", "3": "JP"}
    idioma = idiomas.get(opcao, "PT") # Padrão PT caso o usuário erre
    
    # 3. Lógica para Japonês (Dificuldade)
    dificuldade = None
    if idioma == "JP":
        print("\nEscolha a dificuldade:")
        print("A. Fácil (Romaji)")
        print("B. Médio (Hiragana/Katakana - digite sílabas como 'ka')")
        print("C. Difícil (Kanji - Teclado Virtual)")
        dificuldade = input("Opção: ").upper()

    # 4. Busca da Palavra (O pulo do gato!)
    print("\nBuscando palavra...")
    palavra_data = api_engine.buscar_palavra_online(idioma)
    
    # Se a API falhar, usamos o fallback local do constantes.py
    if not palavra_data:
        print("(Usando dicionário local - offline)")
        palavra_data = random.choice(constantes.PALAVRAS[idioma])
    
    # A partir daqui, vamos iniciar a lógica da forca...
    print(f"Palavra selecionada! Boa sorte.")
    # (Continua...)

if __name__ == "__main__":
    novo_jogo()