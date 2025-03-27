def validarEntrada(mensagem):
    while True:
        valor = input(mensagem)
        if valor:
                return valor
        else:
            print("Digite um valor válido!")

def verificadorPassword(entrada):
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minuscula = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"

    if len(entrada) < 8:
        return False
    else:
        qnt_numeros = 0
        qnt_minuscula = 0
        qnt_maiuscula = 0

        for letra in entrada:
            if letra in maiusculas:
                qnt_maiuscula += 1
            elif letra in minuscula:
                qnt_minuscula += 1
            elif letra in numeros:
                qnt_numeros += 1

        eValido = (qnt_maiuscula >= 1) and (qnt_minuscula >= 1) and (qnt_numeros >= 1)
        return eValido
    
entrada = validarEntrada("Digite uma senha: ")
verificadorPassword(entrada)

if verificadorPassword(entrada):
    print("Senha válida!")
else:
    print("Senha inválida! A senha deve ter pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula e um número.")