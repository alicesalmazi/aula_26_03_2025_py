def quadradoNumero(mensagem):
    try:
        valor = int(input(mensagem))
        if valor == valor:
            return valor
    except ValueError:
        print("Digite um valor válido!")

def calcular(entrada):
    resultado = ""
    while entrada > 0:
        digito = entrada % 10
        resultado = str(pow(digito,2)) + resultado
        entrada //= 10
        
    print(resultado)

entrada = int(input("Digite um valor: "))
calcular(entrada)