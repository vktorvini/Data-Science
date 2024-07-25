print("Calcule Desconto")

preco = int(input('Digite o Valor do Preço: '))
desconto = int(input("Digite o Valor do Desconto que deseja Aplicar: "))
calculo = desconto/100*preco

preco_novo = preco-calculo
print('O preço do produto é de R${} reais e com {}% de desconto é R${} reais'.format(preco,desconto,preco_novo))
