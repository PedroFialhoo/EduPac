# 🎮 EduPac

O **EduPac** é um jogo 2D educativo desenvolvido em Python com a biblioteca Pygame e Pygame_GUI, criado para fortalecer o raciocínio lógico de crianças e adolescentes entre 9 e 14 anos, usando uma abordagem lúdica e tecnológica que auxilia no aprendizado.

## ✨ Sobre o nome

O nome **EduPac** surge da união entre **“Educação”** e **“Pac-Man”**, servindo de inspiração para o estilo do jogo. A proposta é trazer desafios no formato arcade, com movimentação dinâmica e foco na resolução de perguntas e problemas, tornando o aprendizado mais divertido.

## 🎯 Objetivo do jogo

- Movimente o personagem pelo mapa usando as **setas do teclado** ou as teclas **W (cima), A (esquerda), S (baixo), D (direita)**.
- Responda corretamente a pergunta para ganhar pontos.

## 🏆 Sistema de pontuação

- Cada resposta certa concede **100 pontos**.
- Ao acumular **1000 pontos**, o jogador avança para o próximo nível.
- O jogo possui **3 níveis**, cada um com **10 perguntas diferentes**, aumentando progressivamente a dificuldade para incentivar o pensamento crítico e a concentração.

## ❤️ Sistema de vidas

- Cada resposta errada faz o jogador perder **1 vida**.
- Se o fantasma colidir com o jogador ele perde **1 vida**.
- O jogador possui **3 vidas**. Após perder todas, o jogo é encerrado automaticamente, estimulando atenção e raciocínio antes de responder.

## 📌 Condições de encerramento

O jogo é finalizado em três situações:
1. Quando o jogador completa os **3 níveis com sucesso**;
2. Quando o jogador perde todas as vidas;
3. Quando o jogador decide encerrar o jogo manualmente.

## ⚙️ Tecnologias utilizadas

- **Python** – Linguagem de programação principal do projeto.
- **Pygame** – Biblioteca para desenvolvimento de jogos 2D.

## 🗂 Organização do projeto

- Organização em **classes separadas por funcionalidades**).
- Utilização de **ambiente virtual Python** para facilitar a instalação e execução do projeto.
- Controle de versões via **GitHub**.

## 🚀 Como executar o EduPac

1. Clone o repositório:
   - git clone https://github.com/seu-usuario/edupac.git
   - cd edupac
2. Crie e ative um ambiente virtual:
   - python -m venv venv
    # Windows:
   - venv\Scripts\activate
    # macOS/Linux:
   - source venv/bin/activate
3. Instale as dependências do jogo:
   - pip install -r requirements.txt
4. Execute o jogo:
   - python main.py

