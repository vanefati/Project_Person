class Pessoa:
    def __init__(self,*filhos, nome=None, idade=38):#construtor com valores por defeito/default
        self.idade=idade
        self.nome=nome
        self.filhos=list(filhos)

    def cumprimentar(self):
        return f'ola.{id(self)}'#determina forma de cumprimento e cria id

if __name__=='__main__':
    
    #criar instancia joao etc
    joao = Pessoa(nome='Joao',idade=20)
    raquel = Pessoa(nome='Raquel',idade=10)
    vanessa = Pessoa(joao,raquel,nome='Vanessa')
    
    #impressão do método cunmprimentar
    print("\n")
    print(Pessoa.cumprimentar(vanessa))
    print(vanessa.cumprimentar())

    print("\n")
    print(id(vanessa))
    

    print(vanessa.nome)
    print(vanessa.idade)

    print("\nFilhos:")
    for filho in vanessa.filhos:
        print(filho.nome)
    
    vanessa.sobrenome='Moura'
       
    print(joao.__dict__)
    print(vanessa.__dict__)

    Pessoa.olhos=2

    print("\nOlhos:")
    print(vanessa.olhos)
    print(joao.olhos)
    print(raquel.olhos)
    
    print("\n")
    print(id(Pessoa.olhos), id(vanessa.olhos), id(joao.olhos))







