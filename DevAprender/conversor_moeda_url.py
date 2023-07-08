# https://cursos.alura.com.br/forum/topico-projeto-usando-heranca-e-criando-nova-classe-279655
import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f" URL: {self.url}\n URL base: {self.get_url_base()}\n Parâmetros da URL: {self.get_url_parametros()}"

    def __eq__(self, other):
        return self.url == other.url

    @staticmethod
    def sanitiza_url(url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www\.)?bytebank\.com(\.br)?/cambio')
        match = padrao_url.match(self.get_url_base())
        if not match:
            raise ValueError("A URL não é válida")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor


class ConverteMoeda:

    def iniciar(self):
        try:
            self.valor = int(input("Informe o valor em USS para converter em R$: "))
            self.url = f"bytebank.com/cambio?quantidade={self.valor}&moedaOrigem=dolar&moedaDestino=real"
            self.extrator_url = ExtratorURL(self.url)

            print(self.conversao())
            print(f"Os parâmetros da Url são: \n{self.extrator_url}")

        except Exception as err:
            print(err)

    def conversao(self):
        self.VALOR_DOLAR = 5.24
        self.moeda_destino = self.extrator_url.get_valor_parametro("moedaDestino")
        self.quantidade = self.extrator_url.get_valor_parametro("quantidade")

        if self.moeda_destino == 'real':
            moeda_destino = float(self.quantidade) * self.VALOR_DOLAR
            return f"O valor de US${self.quantidade} convertido em reais é: R${moeda_destino:.2f}"
        elif self.moeda_destino == 'dolar':
            moeda_destino = float(self.quantidade) / self.VALOR_DOLAR
            return f"O valor de R${self.quantidade} convertido em dolares é: US${moeda_destino:.2f}"


conversor = ConverteMoeda()
conversor.iniciar()
