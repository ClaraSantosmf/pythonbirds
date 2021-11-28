class Pessoa:
    def __init__ (self, *filhos, nome=None, idade= 21): #método de inicialização dos atributos de dados, atributos de instância e objeto.
                        #Para já criar espaço para atribuir valores, é possível passar o atributo como parâmetro
        self.idade = idade # pode ser passado com atributo de instância já com o valor, que pode ser redistribuido no code ou
        self.nome = nome #colocar a existência de um atributo no vazio None, que deve receber um atributo
        self.filhos = list(filhos)
    def cumprimentar (self): #um método é uma função que pertence a uma class atrelada a um objeto obrigatorialment
        return f'olá {id(self)}' #self é uma convenção, poderia se chamar qualquer coisa

if __name__ == '__main__':
    maria = Pessoa(nome= 'Maria') #criamos o objeto vindo da classe Class Pessoa, atribuims parâmetro para nome aqui.
    ana = Pessoa(maria, nome='Ana')
    print(Pessoa.cumprimentar(maria)) #a passagem do objeto é implicita porque estamos tratando de um método
    print(maria.nome) #pegamos o atributo nome dentro do objeto que recebeu o atributo Maria
    print(maria.nome, maria.idade) #Atribuimos nome, mas pegamos idade como parâmetro já posto no init, não precisou declarar
    maria.nome = 'Clara' #significa que peguei no objeto 'p' o atributo nome e reatribuir a ele novo nome 'Clara'
    print(maria.nome) #atributo redefinido
    for filho in ana.filhos:
        print(filho.nome)
    ana.sobrenome = 'santiago' #Aqui é possível criar um atributo dinâmico que será atribuido apenas ao objeto em que surgiu
    print(ana.__dict__) #O comando dict é possível para verificar quais atributos foram incluidos na instância do objeto
    print(maria.__dict__)


