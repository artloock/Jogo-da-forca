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

def gerar_dica_automatica(palavra_data, idioma):
    # Se a palavra já veio com dica (do seu constantes.py), usa ela
    if isinstance(palavra_data, dict) and 'dica' in palavra_data:
        return palavra_data['dica']
    
    # Se a palavra veio da API (apenas uma string), geramos uma dica baseada na estrutura
    palavra = palavra_data if isinstance(palavra_data, str) else palavra_data.get('romaji', '')
    palavra = palavra.upper()
    
    vogais = sum(1 for letra in palavra if letra in "AEIOU")
    consoantes = len(palavra) - vogais
    
    # Dicas genéricas mas úteis
    if idioma == "PT":
        return f"A palavra tem {len(palavra)} letras, sendo {vogais} vogais e {consoantes} consoantes."
    elif idioma == "EN":
        return f"The word has {len(palavra)} letters ({vogais} vowels and {consoantes} consonants)."
    elif idioma == "JP":
        return f"A leitura dessa palavra tem {len(palavra)} caracteres em Romaji."
    
    return "Sem dicas específicas para esta palavra."

def gerar_dica_automatica(palavra_data, idioma):
    # Se for dicionário (local), usa a dica que escrevemos
    if isinstance(palavra_data, dict) and 'dica' in palavra_data:
        return palavra_data['dica']
    
    # Se for string (API), gera dica técnica
    palavra = palavra_data if isinstance(palavra_data, str) else palavra_data.get('romaji', '')
    palavra = palavra.upper()
    vogais = sum(1 for letra in palavra if letra in "AEIOU")
    
    if idioma == "PT":
        return f"A palavra tem {len(palavra)} letras e {vogais} vogais."
    elif idioma == "EN":
        return f"The word has {len(palavra)} letters and {vogais} vowels."
    return f"Leitura: {palavra.lower()}"
