import json
import os

import sessao
import globalFiles

def register(nome, email, idade):

    data = json.dumps({"nome": nome, "email": email, "idade": idade})

    try:
        with open(globalFiles.json_file, "r+", encoding="utf-8") as file:
            file.seek(0, os.SEEK_END)
            pos = file.tell()

            while pos > 0:
                pos -= 1
                file.seek(pos)
                char = file.read(1)

                if char == ']':
                    file.seek(pos - 2)
                    file.write('},\n\t' + data + '\n]')

                    break
    except FileNotFoundError:
        print("ERRO: Arquivo JSON não foi encontrado.")

    return 0

def login(json_data, email):
    if isinstance(json_data, list):

        for i, usuario in enumerate(json_data):
            
            if usuario.get("email") == email:
                return i
                
    return None

def menu(session_var, data):
    os.system("cls")

    save = True

    if session_var == True:
        print("=======================================")
        print("======== BEM VINDO A SUA CONTA ========")
        
        while True:
            print("=======================================")
            print("1 - Ver suas informações\n2 - Editar perfil\n3 - Logout\n")

            if save == False:
                print("AVISO: Mudanças no perfil não foram salvas.")

            try:
                op = int(input("Digite sua escolha: "))
                os.system("cls")
            except ValueError:
                os.system("cls")
                print("ERRO: A opção digitada deve ser somente um número inteiro.")

            try:
                match op:

                    case 1:
                        print("======== DADOS ========")
                        print(f"Nome: {data['nome']}")
                        print(f"E-mail: {data['email']}")
                        print(f"Idade: {data['idade']}")

                    case 2:
                        print("AVISO: Mudanças em progresso...")

                    case 3:
                        data["nome"] = "?"
                        data["email"] = "?"
                        data["idade"] = 0

                        sessao.status = False

                        print("AVISO: Você saiu da sua conta.")
                        break

                    case _:
                        print("ERRO: Essa opção não existe. Tem certeza que digitou corretamente?")

            except NameError:
                print("ERRO: Ocorreu um erro ao processar sua opção, cheque se a variável de opção foi setada corretamente no código do programa. Se o erro persistir, cheque se a sua opção é um número inteiro.")

    
    else:
        print("ERRO: Não foi possível entrar na sua conta. Você não está logado!")


def configuracoes(save_var, data):
        print("======== EDIÇÃO DE CONTA ========")
        print("Selecione a opção desejada:")

        while True:
            
            print("=======================================")
            print("1 - Editar nome\n2 - Editar e-mail\n3 - Editar idade\n4 - Salvar informações\n5 - Voltar\n")

            
            if save_var == False:
                print("AVISO: Mudanças no perfil não foram salvas.")

            # Solicito para o usuário a escolha de uma opção
            conta = int(input("Digite sua escolha: "))
            os.system("cls")

            
            match conta:
                case 1:
                    print("======== EDIÇÃO DE CONTA ========")
                    data["nome"] = input("Edite seu nome: ")

                    os.system("cls")
                    print("======== EDIÇÃO DE CONTA ========")
                    print("Edição feita com sucesso!")

                    save_var = False
                
                case 2:
                    print("======== EDIÇÃO DE CONTA ========")
                    data["email"] = input("Edite seu e-mail: ")

                    os.system("cls")
                    print("======== EDIÇÃO DE CONTA ========")
                    print("Edição feita com sucesso!")

                    save_var = False

                case 3:
                    print("======== EDIÇÃO DE CONTA ========")
                    print("AVISO: Ao usar a data de nascimento como identificador de idade, pode ocorrer de mostrar a idade que você faria este ano caso não tenha feito.\n")
                    anoNasc = int(input("Digite o ano de nascimento: "))
                    data["idade"] = (2026 - anoNasc)

                    os.system("cls")
                    print("======== EDIÇÃO DE CONTA ========")
                    print("Edição feita com sucesso!")

                    save_var = False
                
                case 4:
                    print("======== EDIÇÃO DE CONTA ========")
                    print("Dados salvos com sucesso!")
                    with open(globalFiles.json_file, "w", encoding="utf-8") as file:
                        save_data = json.dump(data, file)
                    
                    save_var = True

                case 5:
                    break
