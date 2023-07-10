# Desafio com 'Sets'

'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

Lista1 = Funcionários que tem carro e trabalham a noite
Lista2 = Funcionários que tem carro e trabalham durante o dia
Lista3 = Funcionários que não tem carro
'''

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']


def gerar_listas():
    func_carro_noturno = set(tem_carro) & set(turno_noite)
    print(f"Funcionários que tem carro e trabalham a noite: {func_carro_noturno}")

    func_carro_diurno = set(tem_carro).intersection(turno_dia)
    print(f"Funcionários que tem carro e trabalham durante o dia: {func_carro_diurno}")

    func_nao_tem_carro = set(funcionarios).difference(tem_carro)  # func_nao_tem_carro = set(funcionarios) - set(tem_carro)
    print(f"Funcionários que não tem carros: {func_nao_tem_carro}")


if __name__ == '__main__':
    gerar_listas()
