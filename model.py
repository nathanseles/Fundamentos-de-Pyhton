import datetime
import sql
from view import *

cnx = sql.SQL('root', 'root', 'test')

def search(id, password):

    comando = 'Select * form tb_user;'
    dados = cnx.consultar(comando, ())

    for (usuario, senha) in dados:
        if usuario == id and senha == password:
            valid = True
            return [usuario, senha, valid]
    valid = False
    return [valid]

def ask_dta():
    ano = validar_ano()
    mes = validar_mes()
    dia = validar_dia()
    try:
        datetime.date(ano, mes,dia)
        return "{}-{}-{}".format(str(ano), str(mes), str(dia))

    except ValueError:
        print("Data invalida, tente novamente.")
        return ask_dta()


def create():
    ask_stg("Digite o nome do produto: ")
    ask_stg("Digite a marca do produto: ")
    ask_int("Digite a quantidade do produto: ","Quantidade invalida.")
    ask_dta()
