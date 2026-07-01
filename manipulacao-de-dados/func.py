import json
import os

import sessao

def register(nome, email, idade):

    data = json.dumps({"nome": nome, "email": email, "idade": idade})

    with open("dados.json", "r+", encoding="utf-8") as file:
        file.seek(0, os.SEEK_END)
        pos = file.tell()

        while pos > 0:
            pos -= 1
            file.seek(pos)
            char = file.read(1)

            if char == ']':
                file.seek(pos - 2)
                file.write(f',\n\t{data}\n]')

                break

    return 0

def login(json_data, email):
    if isinstance(json_data, list):

        for usuario in json_data:

            if usuario.get("email") == email:
                return True
                
    return False

def menu(session_var, data):
    os.system("cls")

    if session_var == True:
        print("---------------------------------------")
        print("-------- BEM VINDO A SUA CONTA --------")
        
        while True:
            print("---------------------------------------")
            print("1 - Ver suas informações\n2 - Editar perfil\n3 - Logout\n")

            op = int(input("Digite sua escolha: "))
            os.system("cls")

            match op:

                case 1:
                    print("-------- DADOS --------")
                    print(f"Nome: {data['nome']}")
                    print(f"E-mail: {data['email']}")
                    print(f"Idade: {data['idade']}")

                case 2:
                    print("Migrando configurações...")

                case 3:
                    data["nome"] = "?"
                    data["email"] = "?"
                    data["idade"] = 0

                    sessao.status = False

                    print("AVISO: Você saiu da sua conta.")
                    break

                case _:
                    print("ERRO: Essa opção não existe. Tem certeza que digitou corretamente?")

    
    else:
        print("ERRO: Não foi possível entrar na sua conta. Você não está logado!")