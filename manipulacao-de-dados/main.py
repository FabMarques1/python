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
    print("1 - Ver perfil\n2 - Editar configurações\n3 - Sair\n")

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
            configuracoes(save)

        case 3:
            print("Obrigado por testar!")
            break

        case _:
            print("ERRO!\nEssa opção não existe. Tem certeza que digitou corretamente?")



    # Editar o perfil através de uma função

    def configuracoes(save_var):
        print("-------- EDIÇÃO DE CONTA --------")
        print("Selecione a opção desejada:")

        while True:
            
            print("---------------------------------------")
            print("1 - Editar nome\n2 - Editar CPF\n3 - Editar idade\n4 - Salvar informações\n5 - Voltar\n")

            
            if save_var == False:
                print("(Dados modificados não salvos...)\n")

            # Solicito para o usuário a escolha de uma opção
            conta = int(input("Digite sua escolha: "))
            os.system("cls")

            
            match conta:
                case 1:
                    print("-------- EDIÇÃO DE CONTA --------")
                    local_info["nome"] = input("Edite seu nome: ")

                    os.system("cls")
                    print("-------- EDIÇÃO DE CONTA --------")
                    print("Edição feita com sucesso!")

                    save_var = False
                
                case 2:
                    print("-------- EDIÇÃO DE CONTA --------")
                    local_info["cpf"] = input("Edite seu CPF: ")

                    os.system("cls")
                    print("-------- EDIÇÃO DE CONTA --------")
                    print("Edição feita com sucesso!")

                    save_var = False

                case 3:
                    print("-------- EDIÇÃO DE CONTA --------")
                    print("AVISO: Ao usar a data de nascimento como identificador de idade, pode ocorrer de mostrar a idade que você faria este ano caso não tenha feito.\n")
                    anoNasc = int(input("Digite o ano de nascimento: "))
                    local_info["idade"] = (anoAtual - anoNasc)

                    os.system("cls")
                    print("-------- EDIÇÃO DE CONTA --------")
                    print("Edição feita com sucesso!")

                    save_var = False
                
                case 4:
                    print("-------- EDIÇÃO DE CONTA --------")
                    print("Dados salvos com sucesso!")
                    with open("dados.json", "w", encoding="utf-8") as file:
                        save_data = json.dump(local_info, file)
                    
                    save_var = True

                case 5:
                    break

