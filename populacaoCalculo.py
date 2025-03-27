def validarEntrada(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("O valor deve ser maior que 0. Tente novamente.")
        except ValueError:
            print("Digite um valor válido!")

def calculadorPopulacao(populacao, metaPopulacao, porcentual):
    contador = 0
    while populacao < metaPopulacao:
        populacao += int((populacao * (porcentual/100)) + 50)
        contador += 1
    if contador == 0:
        print("A população inicial de Engenheiro Coelho já passou/ igualou-se a meta de habitantes.")
    else:
        print(f"A população inicial de Engenheiro Coelho precisará de {contador} anos para passar de {metaPopulacao} habitantes.")
    
populacao = validarEntrada("Digite um valor inicial de população: ")
metaPopulacao = validarEntrada("Digite um valor meta para a população: ")
porcentual = validarEntrada("Digite um porcentual de aumento da população: ")

calculadorPopulacao(populacao, metaPopulacao, porcentual)