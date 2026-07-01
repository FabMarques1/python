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

# Inicializo com uma mensagem amigável
os.system("cls")
print("---------------------------------------")
print("-------- BEM VINDO A CENTRAL ! --------")

while True:
    print("---------------------------------------")
    print("1 - Criar um perfil\n2 - Entrar em um perfil\n3 - Exibir todos os perfis cadastrados\n4 - Sair\n")

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
            email = input("Digite seu e-mail: ").lower()
            anoNasc = int(input("Digite o ano em que nasceu: "))

            while (anoAtual - anoNasc >= 100) or (anoAtual - anoNasc <= 6):
                os.system("cls")

                print("-------- CRIAÇÃO DE CONTA --------")
                print("ERRO: O ano em que nasceu está fora do comum, preencha seu ano verdadeiro de nascimento.")
                anoNasc = int(input("Digite novamente o ano em que nasceu: "))
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
            print("status da sesao: " + sessao.status)

        case _:
            print("ERRO: Essa opção não existe. Tem certeza que digitou corretamente?")
