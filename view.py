def ask_int(msg, msgerro):
    try:
        number = int(input(msg))
    except ValueError:
        print(msgerro)
        return ask_int(msg, msgerro)
    return number

def ask_float(msg, msgerro):
    try:
        number = float(input(msg))
    except ValueError:
        print(msgerro)
        return ask_float(msg, msgerro)
    return number

def ask_stg(msg):
    try:
        string = input(msg)
    except ValueError:
        return ask_stg(msg)
    return string

def validar_ano():
    ano = ask_int("Ano de fabricação: ",
                  "valor invalido, tente novamente.")

    num = len(str(ano))

    if num == 4:
        return ano
    else:
        print("Ano invalido. Tente novamente.")
        return validar_ano()

def validar_mes():
    mes = ask_int("Digite o mês de fabricação: \nEx: 2 - para Fevereiro\n ",
                  "valor invalido, tente novamente.")

    if mes <= 12 and mes >= 1:
        return mes
    else:
        print("MÊS INVALIDO, TENTE NOVAMENTE.")
        return validar_mes()

def validar_dia():
    dia = ask_int("digite o dia de fabricação: ",
                  "valor invalido, tente novamente.")

    if dia <= 31 and dia >= 1:
        return dia
    else:
        print("DIA INVALIDO, TENTE NOVAMENTE.")
        return validar_dia()
