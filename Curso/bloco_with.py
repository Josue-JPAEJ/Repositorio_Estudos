"""
o bloco with

# o bloco with é utilizado para criar um contexto de
trabalho onde os arquivos utilizados são fechados apos o
bloco with

"""

# o bloco with - forma Pythonica de manipular arquivo

with open ('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)    #retorna false (arquivo esta aberto)

print(arquivo.closed)    #retorna true (arquivo está fechado)
