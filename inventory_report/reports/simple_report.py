from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(lista):
        dt_now = datetime.now()
        qtd_prod_por_empresa = {}
        maior_qtd_prod = 0

        for produto in lista:
            dt_fab_inlist = datetime.strptime(produto["data_de_fabricacao"], "%Y-%m-%d")
            dt_val_inlist = datetime.strptime(produto["data_de_validade"], "%Y-%m-%d")
            nome_da_empresa = produto["nome_da_empresa"]

            if nome_da_empresa not in qtd_prod_por_empresa:
                qtd_prod_por_empresa[nome_da_empresa] = 1
            else:
                qtd_prod_por_empresa[nome_da_empresa] += 1

            if produto == lista[0]:
                dt_fab = dt_fab_inlist
                dt_val = dt_val_inlist
            else:
                if dt_fab_inlist < dt_fab:
                    dt_fab = dt_fab_inlist
                if dt_val_inlist >= dt_now and dt_val_inlist < dt_val:
                    dt_val = dt_val_inlist

        for empresa, qtd_produtos in qtd_prod_por_empresa.items():
            if qtd_produtos > maior_qtd_prod:
                maior_qtd_prod = qtd_produtos
                maior_estque = empresa

        relatorio = """Data de fabricação mais antiga: {1}
Data de validade mais próxima: {2}
Empresa com maior quantidade de produtos estocados: {0}""".format(maior_estque, dt_fab.strftime("%Y-%m-%d"), dt_val.strftime("%Y-%m-%d"))

        return relatorio
