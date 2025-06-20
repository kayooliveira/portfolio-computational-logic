## **Blueprint do Projeto: Sistema de Gerenciamento de Eventos Universitários**

### **1. Título do Projeto**
*   **Portfólio de Desenvolvimento: Sistema de Gerenciamento de Eventos Universitários**

### **2. Objetivo Principal**
*   Desenvolver um sistema de gerenciamento de eventos para a **UniFECAF**.
*   O sistema será utilizado por alunos e coordenadores para organizar e controlar eventos como workshops, palestras e a "Tech Week".
*   Permitir o cadastro, atualização de detalhes, inscrição de usuários em eventos, e exibição da lista de eventos disponíveis e participantes registrados.

### **3. Requisitos / Funcionalidades Essenciais**
O sistema deve implementar as seguintes funcionalidades:
*   **Cadastro de Eventos**: Permitir que o organizador crie novos eventos, incluindo nome, data, descrição e número máximo de participantes.
*   **Atualização de Eventos**: Possibilitar a alteração de informações de eventos já cadastrados, como data ou número de vagas disponíveis.
*   **Visualização de Eventos Disponíveis**: Usuários devem conseguir visualizar eventos com detalhes (nome, data, descrição e vagas restantes).
*   **Inscrição em Eventos**: Alunos podem se inscrever em eventos que estão disponíveis e dentro do limite de vagas.
*   **Visualizar Inscrições**: O organizador pode visualizar a lista de inscritos para cada evento.
*   **Exclusão de Eventos**: Permitir a remoção de eventos cancelados.

### **4. Conceitos de Programação e Boas Práticas (Foco)**
O desenvolvimento deve aplicar e demonstrar o conhecimento nos seguintes conceitos:
*   **Lógica Computacional e Controle de Fluxo**: Fundamentais para a construção do sistema.
*   **Estruturas Condicionais (`IF`, `ELSE`)**: Utilizadas para garantir que o número de vagas não seja excedido, e para outras validações.
*   **Loops (`FOR`, `WHILE`)**: Necessários para exibir listas de eventos e participantes, e para a interface do menu principal.
*   **Estruturas de Dados**: Usar **listas e dicionários** para armazenar dados dos eventos e inscrições de forma estruturada. Pode-se considerar listas de dicionários para eventos e uma estrutura separada para inscrições.
*   **Boas Práticas de Programação**:
    *   **Modularização**: Sugerir a criação de funções dedicadas para cada funcionalidade (ex: `cadastrar_evento()`, `inscrever_aluno()`).
    *   **Organização Clara do Código**: Manter o código limpo e legível.
    *   **Comentários Explicativos**: Adicionar comentários onde a lógica for complexa ou para clarear o propósito do código.
    *   **Nomes de Variáveis Claros**: Utilizar nomes descritivos para variáveis e funções.

### **5. Exemplo de Fluxo (Referência)**
O sistema deve ser capaz de seguir um fluxo semelhante a este:
*   Coordenador adiciona um evento (“Workshop de Programação em Python” com data e vagas).
*   Aluno visualiza eventos disponíveis e se inscreve no workshop.
*   Coordenador verifica a lista de inscritos para o evento.
*   Coordenador atualiza a data de um evento.
*   Coordenador exclui um evento cancelado.

### **6. Entregável**
*   **Código do Sistema**: Um arquivo ou pasta com o código Python (`.py`) implementando o sistema, contendo comentários explicativos e boas práticas de programação.
*   **Link do Vídeo Pitch (até 4 minutos)**: Um vídeo apresentando o sistema, explicando o que ele faz, as principais funcionalidades e mostrando seu funcionamento prático.

---