# main.py
from modules import constantes
from modules import utils
from modules import api_engine
import random

def processar_palpite(idioma, dificuldade):
    tentativa = input("\nDigite seu palpite: ").lower()
    
    # Lógica para Japonês Nível B (Sílaba -> Kana)
    if idioma == "JP" and dificuldade == "B":
        return constantes.ROMAJI_TO_KANA.get(tentativa, tentativa)
    
    return tentativa

def novo_jogo():
    utils.limpar_tela()
    print("Bem-vindo ao Jogo da Forca 2.0!")
    
    # 1. Seleção de Idioma
    print("\nEscolha o idioma / Choose language:")
    print("1. Português (PT)")
    print("2. English (EN)")
    print("3. 日本語 (JP)")
    
    opcao = input("\nOpção: ")
    idiomas = {"1": "PT", "2": "EN", "3": "JP"}
    idioma = idiomas.get(opcao, "PT")
    
    # 2. Dificuldade para Japonês
    dificuldade = None
    if idioma == "JP":
        print("\nEscolha a dificuldade:")
        print("A. Fácil (Romaji)")
        print("B. Médio (Hiragana/Katakana)")
        print("C. Difícil (Kanji)")
        dificuldade = input("Opção: ").upper()

    # 3. Busca da Palavra
    print("\nBuscando palavra...")
    palavra_data = api_engine.buscar_palavra_online(idioma)
    
    if not palavra_data:
        print("(Usando dicionário local - offline)")
        palavra_data = random.choice(constantes.PALAVRAS[idioma])
    
    # 4. Tratamento da palavra alvo
    if idioma == "JP":
        if dificuldade == "A": palavra_alvo = palavra_data['romaji'].lower()
        elif dificuldade == "B": palavra_alvo = palavra_data['kana']
        else: palavra_alvo = palavra_data['kanji']
    else:
        # Garante que palavra_alvo seja string se vier da API ou dict
        palavra_alvo = palavra_data.lower() if isinstance(palavra_data, str) else palavra_data['palavra'].lower()

    # 5. Inicialização de Variáveis (Essencial estar ANTES do while)
    chances = 6
    letras_tentadas = []
    discovered_letters = ['_' for _ in palavra_alvo]
    dica_revelada = True if (idioma == "JP" and dificuldade == "C") else False

    # 6. Loop Principal
    while chances > 0 and "_" in discovered_letters:
        utils.limpar_tela()
        utils.exibir_cabecalho(idioma, dificuldade)
        
        # Exibição da Dica
        if dica_revelada:
            dica = palavra_data.get('dica', 'Sem dica disponível')
            print(f"💡 DICA: {dica}")
        else:
            print("💡 DICA: Pressione [0] para comprar dica (-2 chances)")
            
        print("\nPalavra: ", " ".join(discovered_letters))
        print(f"Chances: {chances} | Tentativas: {', '.join(letras_tentadas)}")

        # Dica extra para Kanji
        if idioma == "JP" and dificuldade == "C":
            print(f"[LEITURA]: A palavra em romaji é: {palavra_data.get('romaji')}")
        
        palpite = processar_palpite(idioma, dificuldade)

        # Lógica de compra de dica
        if palpite == "0" and not dica_revelada:
            if chances > 2:
                chances -= 2
                dica_revelada = True
            continue

        if palpite in letras_tentadas:
            print("Você já tentou essa!")
            input("Pressione Enter...")
            continue

        letras_tentadas.append(palpite)

        # Lógica de Verificação
        if idioma == "JP" and dificuldade == "C":
            if palpite == palavra_data.get('romaji', '').lower():
                discovered_letters = [palavra_data['kanji']]
            else:
                chances -= 1
        else:
            if palpite in palavra_alvo:
                for i, char in enumerate(palavra_alvo):
                    if char == palpite:
                        discovered_letters[i] = char
            else:
                chances -= 1

    # 7. Fim de Jogo
    utils.limpar_tela()
    if "_" not in discovered_letters:
        print(f"✨ Parabéns! Você venceu. A palavra era: {palavra_alvo}")
    else:
        print(f"💀 Game Over! A palavra era: {palavra_alvo}")

if __name__ == "__main__":
    novo_jogo()