# constantes.py

# 1. Listas de Fallback (Caso a internet falhe)
PALAVRAS = {
    "PT": ["BANANA", "ABACAXI", "DESENVOLVEDOR", "PROGRAMAÇÃO", "PYTHON"],
    "EN": ["BANANA", "PINEAPPLE", "DEVELOPER", "PROGRAMMING", "PYTHON"],
    "JP": [
        {"kanji": "猫", "kana": "ねこ", "romaji": "neko"},
        {"kanji": "犬", "kana": "いぬ", "romaji": "inu"},
        {"kanji": "日本", "kana": "にほん", "romaji": "nihon"},
        {"kanji": "食べる", "kana": "たべる", "romaji": "taberu"},
        {"kanji": "水", "kana": "みず", "romaji": "mizu"}
    ]
}

# 2. Mapeamento de Sílabas (Para o Nível B - Japonês)
# Isso permite que o usuário digite 'ka' e o sistema entenda 'か'
ROMAJI_TO_KANA = {
    "ka": "か", "ki": "き", "ku": "く", "ke": "け", "ko": "こ",
    "sa": "さ", "shi": "し", "su": "す", "se": "せ", "so": "そ",
    "ta": "た", "chi": "ち", "tsu": "つ", "te": "て", "to": "と",
    "na": "な", "ni": "に", "nu": "ぬ", "ne": "ね", "no": "の",
    "ha": "は", "hi": "ひ", "fu": "ふ", "he": "へ", "ho": "ほ",
    "ma": "ま", "mi": "み", "mu": "む", "me": "め", "mo": "も",
    "ya": "や", "yu": "ゆ", "yo": "よ",
    "ra": "ら", "ri": "り", "ru": "る", "re": "れ", "ro": "ろ",
    "wa": "わ", "wo": "を", "n": "ん"
}

# 3. Desenho da Forca (Para deixar o main.py limpo)
STAGES = [
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
       -
    """,
    # ... (completar os outros estágios depois)
]