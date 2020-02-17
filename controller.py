from view import ask_int, ask_float, ask_stg
from model import *

funcion = { 1:'create', 2:'reade', 3:'update', 4:'delete',5:'get_out' }
user = 'null'

def check_login():
    identity = ask_stg('Login: ')
    password = ask_int('Senha: ', 'Senha inválida, tente números.')

    valid = search(identity, password)

    if valid[-1]:
        print("Login válido")
        user = (valid[0], valid[1])
        return menu()

    else:
        print("Login inválido, tente novamente!")
        return check_login()


def menu():
    option = ask_int("Dígite: " +
                     "1 - para cadastra produtos" +
                     "2 - para pesquisar Produtos" +
                     "3 - para Atualizar cadastro de produto" +
                     "4 - para Deletar cadastro de produto" +
                     "5 - Sair",
                     "Opção invalida")

    return funcion[option]()

