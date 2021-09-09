from simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self, lista):
        super().__init__(lista)

    def generate(self):
        qtd_prod_por_empresa = {}
        relatorio = super().generate() + "\n\nProdutos estocados por empresa:"
        qtd_prod_por_empresa = CompleteReport.sum_qtd_prod(self.lista)

        for empresa, qtd in qtd_prod_por_empresa.items():
            relatorio = relatorio + "\n- {0}: {1}".format(empresa, qtd)
        return relatorio
