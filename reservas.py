# Listas para guardar as reservas
lista_aviao = []
lista_hotel = []
lista_pacote = []
# Preços
preco_aviao1 = 1500  # Primeira classe
preco_aviao2 = 500   # Econômica

preco_hotel1 = 1000  # Suíte
preco_hotel2 = 400   # Comum
# Pacotes prontos
nome_pacote1 = "Pacote Aventura"
nome_pacote2 = "Pacote Relax"
nome_pacote3 = "Pacote Cultural"

preco_pacote1 = 1500
preco_pacote2 = 1300
preco_pacote3 = 1100
#Reservas
def reservar_aviao():
    print("=== Reserva de Avião ===")
    nome = input("Digite o nome do passageiro: ")
    data = input("Data do voo: ")
    print("1 - Primeira Classe (R$1500)")
    print("2 - Econômica (R$500)")
    tipo = input("Escolha 1 ou 2: ")
    if tipo == "1":
        classe = "Primeira Classe"
        valor = preco_aviao1
    else:
        classe = "Econômica"
        valor = preco_aviao2
    lista_aviao.append([nome, data, classe, valor])
    print("Reserva feita com sucesso!")

def reservar_hotel():
    print("=== Reserva de Hotel ===")
    nome = input("Digite o nome do hóspede: ")
    data = input("Data da hospedagem: ")
    print("1 - Suíte (R$1000)")
    print("2 - Quarto Comum (R$400)")
    tipo = input("Escolha 1 ou 2: ")
    if tipo == "1":
        quarto = "Suíte"
        valor = preco_hotel1
    else:
        quarto = "Quarto Comum"
        valor = preco_hotel2
    lista_hotel.append([nome, data, quarto, valor])
    print("Reserva feita com sucesso!")

def mostrar_pacotes():
    print("=== Pacotes Turísticos ===")
    print("1 - Aventura: Trilha, Tirolesa, Carro 4x4 - R$1500")
    print("2 - Relax: Praia, Massagem, Carro Executivo - R$1300")
    print("3 - Cultural: Museus, Culinária, Carro Popular - R$1100")

def reservar_pacote():
    print("=== Reserva de Pacote ===")
    nome = input("Digite o nome do cliente: ")
    data = input("Data do passeio: ")
    mostrar_pacotes()
    escolha = input("Escolha o pacote (1, 2 ou 3): ")

    if escolha == "1":
        lista_pacote.append([nome, data, nome_pacote1, preco_pacote1])
    elif escolha == "2":
        lista_pacote.append([nome, data, nome_pacote2, preco_pacote2])
    elif escolha == "3":
        lista_pacote.append([nome, data, nome_pacote3, preco_pacote3])
    else:
        print("Opção inválida.")
        return

    print("Reserva do pacote feita!")

#Confirmação de pacote completo
def confirmar_pacote_completo():
    print("=== Confirmar Pacote Completo ===")
    nome = input("Digite o nome do cliente: ")
    total = 0
    achou_aviao = False
    achou_hotel = False
    achou_pacote = False

    for r in lista_aviao:
        if r[0].lower() == nome.lower():
            print(f"Avião: {r[2]}, R${r[3]}")
            total += r[3]
            achou_aviao = True

    for r in lista_hotel:
        if r[0].lower() == nome.lower():
            print(f"Hotel: {r[2]}, R${r[3]}")
            total += r[3]
            achou_hotel = True

    for r in lista_pacote:
        if r[0].lower() == nome.lower():
            print(f"Pacote: {r[2]}, R${r[3]}")
            total += r[3]
            achou_pacote = True

    if achou_aviao and achou_hotel and achou_pacote:
        print(f"{nome} tem o pacote completo!")
        print(f"Total: R${total}")
    else:
        print("Faltam reservas para completar o pacote.")
# Menu simples
def menu():
    while True:
        print("\n==== MENU ====")
        print("1 - Reservar Avião")
        print("2 - Reservar Hotel")
        print("3 - Reservar Pacote")
        print("4 - Confirmar Pacote Completo")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            reservar_aviao()
        elif opcao == "2":
            reservar_hotel()
        elif opcao == "3":
            reservar_pacote()
        elif opcao == "4":
            confirmar_pacote_completo()
        elif opcao == "0":
            print("Boa Viagem!")
            break
        else:
            print("Opção errada. Tente de novo.")

# Iniciar o programa
menu()