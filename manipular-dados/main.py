import json
import os

# Abrindo arquivo JSON
with open("dados.json", "r", encoding="utf-8") as file:
    global_temp_info = json.load(file)

# Declarando dados locais
local_info = {
    "nome": global_temp_info["nome"],
    "cpf": global_temp_info["cpf"],
    "idade": global_temp_info["idade"]
}

# Declaro o ano atual
anoAtual = 2026

# Declarando alerta de salvamento
save = True

# Inicializo com uma mensagem amigável
print("---------------------------------------")
print("-------- BEM VINDO A SUA CONTA --------")

while True:
    print("---------------------------------------")
    print("1 - Ver seus dados locais\n2 - Editar seu nome\n3 - Editar seu CPF\n4 - Editar sua idade\n5 - Salvar informações\n6 - Sair\n")

    if save == False:
        print("(Dados modificados não salvos...)\n")

    # Solicito para o usuário a escolha de uma opção
    op = int(input("Digite sua escolha: "))
    os.system("cls")

    # A opção é procurada com base nos casos existentes
    # Match-Case = Switch-Case
    match op:
        case 1:
            print("-------- DADOS --------")
            print(f"Nome: {local_info['nome']}")
            print(f"CPF: {local_info['cpf']}")
            print(f"Idade: {local_info['idade']}")

        case 2:
            print("-------- EDIÇÃO --------")
            local_info["nome"] = input("Edite seu nome: ")

            save = False
        
        case 3:
            print("-------- EDIÇÃO --------")
            local_info["cpf"] = input("Edite seu CPF: ")

            save = False

        case 4:
            print("-------- EDIÇÃO --------")
            print("AVISO: Ao usar a data de nascimento como identificador de idade, pode ocorrer de mostrar a idade que você faria este ano caso não tenha feito.\n")
            anoNasc = int(input("Digite o ano de nascimento: "))
            local_info["idade"] = (anoAtual - anoNasc)

            save = False
        
        case 5:
            print("-------- SALVANDO --------")
            print("Dados salvos com sucesso!")
            file = open("dados.json", "w", encoding="utf-8")
            save_data = json.dump(local_info, file)
            file.close()

            save = True

        case 6:
            print("Obrigado por testar!")
            break

        case _:
            print("ERRO!\nEssa opção não existe. Tem certeza que digitou corretamente?")
