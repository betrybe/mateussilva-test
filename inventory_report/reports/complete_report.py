from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    # Utilizar mesma lógica de SimpleReport, mas agora adicionar a quantidade
    # de produtos por empresa ao final
    def generate(lista):
        qtd_prod_por_empresa = {}
        relatorio = (
            SimpleReport.generate(lista)
            + "\nProdutos estocados por empresa: \n"
        )
        qtd_prod_por_empresa = CompleteReport.sum_qtd_prod(lista)

        for empresa, qtd in qtd_prod_por_empresa.items():
            relatorio = relatorio + "- {0}: {1}\n".format(empresa, qtd)
        return relatorio
