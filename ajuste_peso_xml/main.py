import os
import xml.etree.ElementTree as et
from datetime import datetime as dt

diretorio_origem = os.getcwd()
diretorio_destino = f'{diretorio_origem}\\xml {dt.now().day}-{dt.now().month}-{dt.now().year}'


def arredondar_peso_xml(arquivo_xml: str) -> None:
    nome_novo_arquivo = f'{diretorio_destino}\\peso_ajustado_{arquivo_xml}'
    edicao = False

    try:
        xml = et.parse(arquivo_xml)
        root = xml.getroot()

        for item in root.findall('.//'):

            if 'pesoB' in item.tag:
                item.text = str(round(float(item.text)))
                edicao = True
            elif 'pesoL' in item.tag:
                edicao = True
                item.text = str(round(float(item.text)))

        for elem in xml.iter():
            elem.tag = elem.tag.split('}')[-1]

        if edicao:
            xml.write(nome_novo_arquivo)

    except Exception as err:
        print(err)


if __name__ == '__main__':

    if not os.path.isdir(diretorio_destino):
        os.mkdir(diretorio_destino)

    for arquivo in os.listdir(diretorio_origem):
        if arquivo.lower().endswith('.xml'):
            arredondar_peso_xml(arquivo)
