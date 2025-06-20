# Portfólio de Desenvolvimento: Sistema de Gerenciamento de Eventos Universitários

Este projeto faz parte do portfólio da disciplina de **Lógica Computacional**, demonstrando a aplicação de conceitos fundamentais de programação em Python para resolver um problema prático.

## 🎯 Objetivo do Projeto

O objetivo é desenvolver um sistema de controle para a **UniFECAF**, permitindo a organização e o controle de eventos acadêmicos como workshops, palestras e a "Tech Week". O sistema deve ser intuitivo para coordenadores e alunos, centralizando as operações de gerenciamento de eventos e inscrições.

## ✨ Funcionalidades Implementadas

O sistema oferece um menu interativo com as seguintes funcionalidades:

1.  **Cadastrar Evento**: Adiciona um novo evento ao sistema, solicitando:
    -   Nome do Evento
    -   Data
    -   Descrição
    -   Número Máximo de Participantes

2.  **Visualizar Eventos Disponíveis**: Exibe uma lista formatada de todos os eventos, mostrando nome, data, vagas restantes e descrição.

3.  **Atualizar Evento**: Permite modificar as informações de um evento existente (data, descrição, número de vagas).

4.  **Inscrever-se em um Evento**: Permite que um participante se inscreva em um evento, validando a disponibilidade de vagas.

5.  **Visualizar Inscrições de um Evento**: Mostra a lista de todos os participantes inscritos em um evento específico.

6.  **Excluir Evento**: Remove um evento do sistema após confirmação.

7.  **Sair**: Encerra a execução do programa.

## 🛠️ Tecnologias e Conceitos Aplicados

-   **Linguagem**: Python 3
-   **Estrutura de Dados**: A base de dados em memória é uma **lista de dicionários**, onde cada dicionário representa um evento e contém suas informações, incluindo uma lista aninhada para os participantes.
-   **Lógica de Programação**:
    -   Uso intensivo de **funções** para modularizar o código.
    -   **Estruturas condicionais (`if/elif/else`)** para validações de dados e controle de fluxo.
    -   **Loops (`for`, `while`)** para percorrer a lista de eventos e manter o menu principal em execução.
-   **Interface de Usuário**:
    -   Interface de linha de comando (CLI) interativa e amigável.
    -   Uso de **cores** para melhorar a legibilidade e a experiência do usuário, destacando mensagens de sucesso, erro e informação.
    -   Menus, mensagens de erro/confirmações e títulos melhorados para deixar mais intuitivo.
    -   O terminal é limpo a cada interação para manter a interface limpa e organizada. 
## 🚀 Como Executar

Para executar o sistema, você precisa ter o Python 3 instalado em sua máquina. Siga os passos abaixo:

1.  **Clone o repositório** (ou baixe os arquivos):
    ```bash
    git clone https://github.com/kayooliveira/portfolio-computational-logic.git
    ```

2.  **Navegue até o diretório do projeto**:
    ```bash
    cd portfolio-computational-logic
    ```

3.  **Execute o script principal**:
    ```bash
    python sistema_eventos.py
    ```

Após a execução, o menu principal do sistema será exibido no terminal, e você poderá interagir com as opções disponíveis.

---

## 👨‍💻 Autor

- **Nome**: Kayo Oliveira
- **Instagram**: [@kayooliveiradev](https://instagram.com/kayooliveiradev)
