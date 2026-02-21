🎮 Jogo da Forca Poliglota 2.0
Um projeto de Jogo da Forca robusto desenvolvido em Python, com foco em modularização, consumo de APIs externas e lógica avançada para múltiplos idiomas.

📂 Estrutura do Projeto
O projeto foi refatorado para seguir uma arquitetura limpa:

main.py: Ponto de entrada e controle do loop do jogo.

modules/:

api_engine.py: Gerencia as requisições HTTP para buscar palavras online.

constantes.py: Armazena dicionários locais, mapeamentos de caracteres (Romaji -> Kana) e configurações.

utils.py: Funções auxiliares para limpeza de tela, cabeçalhos e geração de dicas automáticas.

Pseudocódigo.txt: Documentação da lógica algorítmica do sistema.

🚀 Funcionalidades
Modo Online: Busca automática de palavras em Português e Inglês via API.

Modo Offline: Fallback para dicionário local caso a conexão falhe.

Sistema de Dicas: O jogador pode comprar dicas técnicas (baseadas na estrutura da palavra) em troca de 2 chances.

Suporte a Japonês: Três níveis de dificuldade (Romaji, Hiragana e Kanji).

🚧 Status de Desenvolvimento (Bugs Conhecidos)
Atualmente, o núcleo do jogo em Português e Inglês está 100% funcional. Os seguintes pontos estão em fase de correção:

Japonês Nível B (Sílaba): A conversão dinâmica de Romaji para Kana está em refinamento para garantir que o sistema revele corretamente os caracteres no tabuleiro.

Japonês Nível C (Kanji): A lógica de entrada de texto completo (Romaji validando Kanji) está sendo estabilizada para evitar erros de comparação de strings.

🛠️ Como Executar
Instale a biblioteca necessária:

PowerShell
python -m pip install requests
Inicie o jogo:

PowerShell
python main.py