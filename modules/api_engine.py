import requests
import random

def buscar_palavra_online(idioma):
    """
    Busca uma palavra aleatória via API baseada no idioma.
    Retorna a palavra (string ou dict para JP) ou None se falhar.
    """
    urls = {
        "PT": "https://api.dicionario-aberto.net/random", # API de Português
        "EN": "https://random-word-api.herokuapp.com/word?number=1", # API de Inglês
        "JP": "https://random-words-api.vercel.app/word/japanese" # API de Japonês
    }

    try:
        # Definimos um timeout de 3 segundos para o jogo não travar se a net estiver lenta
        response = requests.get(urls.get(idioma), timeout=3)
        
        if response.status_code == 200:
            dados = response.json()
            
            if idioma == "PT":
                return dados['word'].upper()
            elif idioma == "EN":
                return dados[0].upper()
            elif idioma == "JP":
                # A API de Japonês geralmente retorna um array com dict: 
                # [{"word": "猫", "furigana": "ねこ", "romaji": "neko"}]
                return {
                    "kanji": dados[0]['word'],
                    "kana": dados[0]['furigana'],
                    "romaji": dados[0]['romaji']
                }
    except Exception:
        return None # Indica que houve erro e o jogo deve usar o fallback local