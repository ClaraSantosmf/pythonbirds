class Pessoa:
    def __init__ (self, nome=None, idade= 21): #método de inicialização dos atributos de dados, atributos de instância e objeto.
                        #Para já criar espaço para atribuir valores, é possível passar o atributo como parâmetro
                        self.idade = idade # pode ser passado com atributo de instância já com o valor, que pode ser redistribuido no code ou
                        self.nome = nome #colocar a existência de um atributo no vazio None, que deve receber um atributo
    def cumprimentar (self): #um método é uma função que pertence a uma class atrelada a um objeto obrigatorialment
        return f'olá {id(self)}' #self é uma convenção, poderia se chamar qualquer coisa

if __name__ == '__main__':
    p = Pessoa('Maria') #criamos o objeto vindo da classe Class Pessoa, atribuims parâmetro para nome aqui.
    print(p.cumprimentar()) #a passagem do objeto é implicita porque estamos tratando de um método
    print(p.nome) #pegamos o atributo nome dentro do objeto que recebeu o atributo Maria
    print(p.nome, p.idade) #Atribuimos nome, mas pegamos idade como parâmetro já posto no init, não precisou declarar
    p.nome = 'Clara' #significa que peguei no objeto 'p' o atributo nome e reatribuir a ele novo nome 'Clara'
    print(p.nome) #atributo redefinido

