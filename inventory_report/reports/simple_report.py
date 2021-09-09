from datetime import datetime


class SimpleReport:
    def __init__(self, lista):
        self.lista = lista

    # Função para somar todas os produtos de uma mesma empresa e retorna um
    # dicionário com esses valores {"nome_da_empresa":"quantidade_de_produtos"}
    def sum_qtd_prod(lista):
        qtd_prod_por_empresa = {}
        for produto in lista:
            nome_da_empresa = produto["nome_da_empresa"]
            if nome_da_empresa not in qtd_prod_por_empresa:
                qtd_prod_por_empresa[nome_da_empresa] = 1
            else:
                qtd_prod_por_empresa[nome_da_empresa] += 1
        return qtd_prod_por_empresa

    # Função para validar a data de fabricação mais antiga e a data de validade
    # mais proxima dentro de uma lista de produtos
    # retornando essas datas

    def check_fab_val(lista):
        dt_fab = dt_val = dt_now = datetime.now()
        for produto in lista:
            dt_fab_inlist = datetime.strptime(produto["data_de_fabricacao"], "%Y-%m-%d")
            dt_val_inlist = datetime.strptime(produto["data_de_validade"], "%Y-%m-%d")
            if produto == lista[0]:
                dt_fab = dt_fab_inlist
                dt_val = dt_val_inlist
            else:
                if dt_fab_inlist < dt_fab:
                    dt_fab = dt_fab_inlist
                if dt_val_inlist >= dt_now and dt_val_inlist < dt_val:
                    dt_val = dt_val_inlist
        return dt_fab, dt_val

    # Função para comparar qual empresa possui maior quantidade de produtos
    # retornando o nome dessa empresa

    def ckeck_prod_empresa(qtd_prod_por_empresa):
        maior_qtd_prod = 0
        for empresa, qtd_produtos in qtd_prod_por_empresa.items():
            if qtd_produtos > maior_qtd_prod:
                maior_qtd_prod = qtd_produtos
                empresa_maior_estoque = empresa
        return empresa_maior_estoque

    def generate(self):
        # Sumarizando quantidades de produtos por empresa
        qtd_prod_por_empresa = SimpleReport.sum_qtd_prod(self.lista)
        # Validando datas de valiade e fabricação
        dt_fab, dt_val = SimpleReport.check_fab_val(self.lista)
        # Comparando estoques
        empresa_mais_prod = SimpleReport.ckeck_prod_empresa(qtd_prod_por_empresa)

        relatorio = """Data de fabricação mais antiga: {0}
Data de validade mais próxima: {1}
Empresa com maior quantidade de produtos estocados: {2}""".format(dt_fab.strftime("%Y-%m-%d"), dt_val.strftime("%Y-%m-%d"), empresa_mais_prod)
        return relatorio
