# constantes.py

# 1. Listas de Fallback (Caso a internet falhe)
PALAVRAS = {
    "PT": [
        {"palavra": "BANANA", "dica": "Uma fruta amarela"},
        {"palavra": "DESENVOLVEDOR", "dica": "Quem transforma café em código"}
    ],
    "EN": [
        {"palavra": "PINEAPPLE", "dica": "A tropical fruit with a crown"},
        {"palavra": "DEVELOPER", "dica": "Someone who writes software"}
    ],
    "JP": [
        {"kanji": "猫", "kana": "ねこ", "romaji": "neko", "dica": "Um animal que faz 'miau'"},
        {"kanji": "水", "kana": "mizu", "romaji": "mizu", "dica": "Essencial para a vida, você bebe"}
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