def quadradoNumero(mensagem):
    try:
        valor = int(input(mensagem))
        if valor == valor:
            return valor
    except ValueError:
        print("Digite um valor válido!")

def calcular(entrada):
    texto = ""
    while entrada > 0:
        digito = entrada % 10
        texto = str(pow(digito,2)) + texto
        entrada //= 10

    resultado = int(texto) if texto != "" else 0
    print(resultado)

entrada = quadradoNumero("Digite um valor: ")
calcular(entrada)
