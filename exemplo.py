class Produto():
    def __init__(self, nome, preco,unidade):
        self.nome = nome
        self.preco = preco
        self.unidade = unidade
    
    def exibir(self):
        print(f'Nome: {self.nome} - Preço: {self.preco}')


produto = Produto('Pizza', 5, 'unidade')

produto.exibir()

quantidade = int(input('Informe a quantidade: '))

        
