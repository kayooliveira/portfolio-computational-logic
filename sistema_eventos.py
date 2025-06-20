"""
Aluno: Kayo Víctor Oliveira da Silva Viana
Data: 20/06/2025
Versão: 1.0

Sistema de Gerenciamento de Eventos Universitários - UniFECAF
Desenvolvido como parte do portfólio de Lógica Computacional.

Este sistema permite o gerenciamento completo de eventos, incluindo cadastro,
atualização, visualização, inscrição de participantes e exclusão, com uma
interface de usuário colorida e amigável no terminal.
"""

# Estrutura de dados principal para armazenar os eventos.
# Usaremos uma lista de dicionários, onde cada dicionário representa um evento.
# Eu deixei alguns eventos pré-cadsatrados para facilitar os testes.
eventos = [
    {
        'nome': 'Festa de Aniversário UniFECAF',
        'data': '15/07/2025',
        'descricao': 'Celebração do aniversário da universidade com música, comida e diversão.',
        'vagas_maximas': 200,
        'participantes': []
    },
    {
        'nome': 'Palestra sobre Sustentabilidade',
        'data': '22/07/2025',
        'descricao': 'Palestra com especialistas sobre práticas sustentáveis no dia a dia.',
        'vagas_maximas': 100,
        'participantes': []
    }
]

# --- Cores para o Terminal ---
class Cores:
    RESET = "\033[0m"
    VERMELHO = "\033[31m"
    VERDE = "\033[32m"
    AMARELO = "\033[33m"
    AZUL = "\033[34m"
    CIANO = "\033[36m"

# --- Funções Auxiliares de Interface ---
def print_sucesso(mensagem):
  print("\033c", end="")  # Limpa o terminal antes de imprimir a mensagem
  """Imprime uma mensagem de sucesso em verde."""
  barra = f"{Cores.VERDE}{'-' * (len(mensagem) + 8)}{Cores.RESET}"
  print(barra)
  print(f"{Cores.VERDE}  {mensagem.center(len(mensagem) + 4)}  {Cores.RESET}")
  print(barra)

def print_erro(mensagem):
  print("\033c", end="")  # Limpa o terminal antes de imprimir a mensagem
  """Imprime uma mensagem de erro em vermelho."""
  barra = f"{Cores.VERMELHO}{'-' * (len(mensagem) + 8)}{Cores.RESET}"
  print(barra)
  print(f"{Cores.VERMELHO}  {mensagem.center(len(mensagem) + 4)}  {Cores.RESET}")
  print(barra)

def print_info(mensagem):
  """Imprime uma mensagem de informação em ciano."""
  barra = f"{Cores.CIANO}{'-' * (len(mensagem) + 8)}{Cores.RESET}"
  print(barra)
  print(f"{Cores.CIANO}  {mensagem.center(len(mensagem) + 4)}  {Cores.RESET}")
  print(barra)

def print_titulo(titulo):
  """Imprime um título formatado em amarelo."""
  barra = f"{Cores.AMARELO}{'=' * (len(titulo) + 12)}{Cores.RESET}"
  print(barra)
  print(f"{Cores.AMARELO}   --- {titulo} ---   {Cores.RESET}")
  print(barra)

def esperar_usuario():
    """Pausa a execução e espera o usuário pressionar Enter para continuar."""
    input(f"\n{Cores.CIANO}Pressione Enter para voltar ao menu...{Cores.RESET}")

# --- Funções para Gerenciamento de Eventos ---

def cadastrar_evento():
    """Solicita os dados de um novo evento e o adiciona à lista de eventos."""
    print_titulo("Cadastro de Novo Evento")
    
    nome = input("Nome do Evento: ").strip().title()
    if not nome:
        print_erro("O nome do evento não pode ser vazio. Operação cancelada.")
        return

    for evento in eventos:
        if evento['nome'].lower() == nome.lower():
            print_erro(f"O evento '{nome}' já está cadastrado.")
            return

    data = input("Data do Evento (ex: DD/MM/AAAA): ").strip()
    descricao = input("Descrição do Evento: ").strip()
    
    try:
        vagas_maximas = int(input("Número Máximo de Participantes: "))
        if vagas_maximas <= 0:
            print_erro("O número de vagas deve ser um valor positivo.")
            return
    except ValueError:
        print_erro("Número de vagas inválido. Use apenas números inteiros.")
        return

    novo_evento = {
        'nome': nome,
        'data': data,
        'descricao': descricao,
        'vagas_maximas': vagas_maximas,
        'participantes': []  # Lista para armazenar os inscritos
    }
    eventos.append(novo_evento)
    print_sucesso(f"Evento '{nome}' cadastrado com sucesso!")

def visualizar_eventos(pausar=True):
    """Exibe todos os eventos disponíveis com suas informações."""
    print("\033c", end="")  # Limpa o terminal antes de imprimir os eventos
    print_titulo("Eventos Disponíveis")
    if not eventos:
        print_info("Nenhum evento cadastrado no momento.")
        if pausar:
            esperar_usuario()
        return

    print(f"{Cores.AZUL}{'Nome do Evento':<30} {'Data':<15} {'Vagas Restantes':<20} {'Descrição'}{Cores.RESET}")
    print("-" * 80)
    for evento in eventos:
        vagas_restantes = evento['vagas_maximas'] - len(evento['participantes'])
        print(f"{evento['nome']:<30} {evento['data']:<15} {vagas_restantes:<20} {evento['descricao']}")
    
    if pausar:
        esperar_usuario()

def atualizar_evento():
    """Busca um evento pelo nome e permite atualizar suas informações."""
    visualizar_eventos(pausar=False)  # Mostra os eventos para o usuário escolher
    print_titulo("Atualização de Evento")
    nome_evento = input("Nome do evento a ser atualizado: ").strip().title()

    for evento in eventos:
        if evento['nome'].lower() == nome_evento.lower():
            print_info(f"Atualizando o evento: {evento['nome']}. Deixe em branco para não alterar.")
            
            nova_data = input(f"Nova Data ({evento['data']}): ").strip()
            nova_descricao = input(f"Nova Descrição ({evento['descricao']}): ").strip()
            
            try:
                novas_vagas_str = input(f"Novo Nº Máximo de Vagas ({evento['vagas_maximas']}): ").strip()
                if novas_vagas_str:
                    novas_vagas = int(novas_vagas_str)
                    if novas_vagas < len(evento['participantes']):
                        print_erro(f"O novo número de vagas ({novas_vagas}) não pode ser menor que o número de inscritos ({len(evento['participantes'])}).")
                        return
                    evento['vagas_maximas'] = novas_vagas
            except ValueError:
                print_erro("Número de vagas inválido. A atualização das vagas foi ignorada.")

            if nova_data:
                evento['data'] = nova_data
            if nova_descricao:
                evento['descricao'] = nova_descricao
            
            print_sucesso(f"Evento '{nome_evento}' atualizado com sucesso!")
            return
            
    print_erro("Evento não encontrado.")

def excluir_evento():
    """Remove um evento da lista com base no nome."""
    visualizar_eventos(pausar=False)  # Mostra os eventos para o usuário escolher
    print_titulo("Exclusão de Evento")
    nome_evento = input("Nome do evento a ser excluído: ").strip().title()

    for i, evento in enumerate(eventos):
        if evento['nome'].lower() == nome_evento.lower():
            confirmacao = input(f"Tem certeza que deseja excluir o evento '{evento['nome']}'? (s/n): ").strip().lower()
            if confirmacao == 's':
                del eventos[i]
                print_sucesso(f"Evento '{nome_evento}' removido com sucesso!")
            else:
                print_info("Exclusão cancelada.")
            return
            
    print_erro("Evento não encontrado.")

# --- Funções para Gerenciamento de Inscrições ---

def inscrever_em_evento():
    """Inscreve um participante em um evento, se houver vagas."""
    visualizar_eventos(pausar=False) # Mostra os eventos para o usuário escolher
    print_titulo("Inscrição em Evento")
    if not eventos:
        return

    nome_evento = input("\nDigite o nome do evento para se inscrever: ").strip().title()

    for evento in eventos:
        if evento['nome'].lower() == nome_evento.lower():
            vagas_restantes = evento['vagas_maximas'] - len(evento['participantes'])
            if vagas_restantes > 0:
                nome_participante = input("Digite o seu nome completo: ").strip().title()
                if not nome_participante:
                    print_erro("O nome do participante não pode ser vazio.")
                    return
                evento['participantes'].append(nome_participante)
                print_sucesso(f"Inscrição de '{nome_participante}' no evento '{nome_evento}' realizada com sucesso!")
            else:
                print_erro("Não há vagas disponíveis para este evento.")
            return
            
    print_erro("Evento não encontrado.")

def visualizar_inscricoes():
    """Mostra a lista de participantes inscritos em um evento específico."""
    visualizar_eventos(pausar=False)  # Mostra os eventos para o usuário escolher
    print_titulo("Visualizar Inscrições")
    nome_evento = input("\nDigite o nome do evento para ver os inscritos: ").strip().title()

    evento_encontrado = None
    for ev in eventos:
        if ev['nome'].lower() == nome_evento.lower():
            evento_encontrado = ev
            break

    if evento_encontrado:
        print_info(f"Participantes inscritos em '{evento_encontrado['nome']}':")
        if evento_encontrado['participantes']:
            for i, participante in enumerate(evento_encontrado['participantes']):
                print(f"  {i+1}. {participante}")
        else:
            print_info("  Nenhum participante inscrito neste evento.")
    else:
        print(f"{Cores.VERMELHO}Evento não encontrado.{Cores.RESET}")

    esperar_usuario()

# --- Função Principal (Menu) ---

def main():
    """Função principal que exibe o menu e gerencia a interação com o usuário."""
    while True:
        print_titulo("Sistema de Gerenciamento de Eventos UniFECAF")
        print(f"{Cores.AZUL}1.{Cores.RESET} Cadastrar Evento")
        print(f"{Cores.AZUL}2.{Cores.RESET} Visualizar Eventos Disponíveis")
        print(f"{Cores.AZUL}3.{Cores.RESET} Atualizar Evento")
        print(f"{Cores.AZUL}4.{Cores.RESET} Inscrever-se em um Evento")
        print(f"{Cores.AZUL}5.{Cores.RESET} Visualizar Inscrições de um Evento")
        print(f"{Cores.AZUL}6.{Cores.RESET} Excluir Evento")
        print(f"{Cores.AZUL}7.{Cores.RESET} Sair do Sistema")

        try:
            opcao = int(input(f"\n{Cores.CIANO}Escolha uma opção:{Cores.RESET} "))

            if opcao == 1:
                cadastrar_evento()
            elif opcao == 2:
                visualizar_eventos()
            elif opcao == 3:
                atualizar_evento()
            elif opcao == 4:
                inscrever_em_evento()
            elif opcao == 5:
                visualizar_inscricoes()
            elif opcao == 6:
                excluir_evento()
            elif opcao == 7:
                print_sucesso("Saindo do sistema. Até logo!")
                break
            else:
                print_erro("Opção inválida. Por favor, escolha um número do menu.")
        except ValueError:
            print_erro("Entrada inválida. Por favor, insira um número.")

# --- Ponto de Entrada do Programa ---

if __name__ == "__main__":
    main()
