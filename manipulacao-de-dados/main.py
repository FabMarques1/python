# Bibliotecas nativas
import json
import os

# Arquivo local
import func
import sessao

# Declarando dados locais
local_info = {
    "nome": "?",
    "email": "?",
    "idade": 0
}

# Declaro o ano atual
anoAtual = 2026

# Declarando alerta de salvamento
save = True

# Inicializo com uma mensagem amigável
print("---------------------------------------")
print("-------- BEM VINDO A CENTRAL ! --------")

while True:
    print("---------------------------------------")
    print("1 - Criar um perfil\n2 - Entrar em um perfil\n3 - Exibir todos os perfis cadastrados\n4 - Sair\n")

    if save == False:
        print("(Dados modificados não salvos...)\n")

    if sessao.status == True:
        print("Você está logado!")

    # Solicito para o usuário a escolha de uma opção
    op = int(input("Digite sua escolha: "))
    os.system("cls")

    # A opção é procurada com base nos casos existentes
    # Match-Case = Switch-Case
    match op:
        case 1:
            print("-------- CRIAÇÃO DE CONTA --------")
            nome = input("Digite seu nome: ")
            emailRegister = input("Digite seu e-mail: ")
            anoNasc = int(input("Digite o ano em que nasceu: "))

            while (anoAtual - anoNasc >= 100) or (anoAtual - anoNasc <= 6):
                os.system("cls")

                print("-------- CRIAÇÃO DE CONTA --------")
                print("ERRO: O ano em que nasceu está fora do comum, preencha seu ano verdadeiro de nascimento.")
                anoNasc = int(input("Digite novamente o ano em que nasceu: "))

            email = emailRegister.lower()
            idade = (anoAtual - anoNasc)

            func.register(nome, email, idade)

        case 2:
            email = input("Insira seu e-mail: ")

            with open("dados.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                results = func.login(data, email.lower())

                if results:
                    local_info = {
                        "nome": data[0]["nome"],
                        "email": data[0]["email"],
                        "idade": data[0]["idade"]
                    }
                    
                    sessao.status = True
                    func.menu(sessao.status, local_info)
                else:
                    os.system("cls")
                    print("ERRO: Informações não reconhecidas.")

        case 3:
            with open("dados.json", "r", encoding="utf-8") as file:
                global_temp_info = json.load(file)

            print("-------- LISTAGEM DE CONTAS --------")
            for item in global_temp_info:
                if item["nome"] == "":
                    break
                
                print(item["nome"])

        case 4:
            print("Obrigado por testar!")
            break

        case 5:
            print(f"nome de sesao: \n{local_info['nome']}")
            print(sessao.status)

        case _:
            print("ERRO: Essa opção não existe. Tem certeza que digitou corretamente?")

def configuracoes(save_var):
        print("-------- EDIÇÃO DE CONTA --------")
        print("Selecione a opção desejada:")

        while True:
            
            print("---------------------------------------")
            print("1 - Editar nome\n2 - Editar e-mail\n3 - Editar idade\n4 - Salvar informações\n5 - Voltar\n")

            
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
                    local_info["email"] = input("Edite seu e-mail: ")

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

# precisar depois

# print("-------- DADOS --------")
# print(f"Nome: {local_info['nome']}")
# print(f"CPF: {local_info['cpf']}")
# print(f"Idade: {local_info['idade']}")