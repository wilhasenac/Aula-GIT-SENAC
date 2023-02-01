class Produto():
    def __init__(self, nome, preco,unidade):
        self.nome = nome
        self.preco = preco
        self.unidade = unidade
    
    def exibir(self, indice = 0):
        print(f'{indice} == Nome: {self.nome} - Preço: {self.preco}')


produto_um = Produto('Pizza', 5, 'unidade')
produto_dois = Produto('Tomate', 2, 'kilo')

produtos = [produto_um, produto_dois]

for produto in produtos:
    indice = produtos.index(produto)
    produto.exibir(indice)

indice_selecionado = int(input('Selecione o produto: '))

if indice_selecionado > len(produtos)-1:
    print('Produto inexistente')
else:
    produto = produtos[indice_selecionado]
    quantidade = int(input('Informe a quantidade: '))
    print(f'O valor total é: R${quantidade * produto.preco}')


        
