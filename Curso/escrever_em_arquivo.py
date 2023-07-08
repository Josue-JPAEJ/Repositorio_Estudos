"""
Escrevendo em arquivos

OBS: ao abrir um arquivo para leitura não podemos realizar a escrita nele
da mesma forma, se abrir um arquivo para escrita, não podemos lê-lo, somente escrever

ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional

"""

"""
#Exemplo de escrita - w - write (escrita)

with open ('novo.txt', 'w') as arquivo:
    arquivo.write('novos dados.\n')
    arquivo.write('escrevi na proxima linha cem vezes.\n' * 100)
    arquivo.write('esta e a ultima linha')

"""

with open ('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break

