from unit_tests_101.data_model.models.fatura_model import Fatura


class FaturaBuilder:
    def __init__(self):
        self.dados_fatura = Fatura()

    def build_response(self):
        self.dados_fatura.Faturado = self.get_valor_faturado()
        self.dados_fatura.Ajuste = self.get_valor_ajuste()
        self.dados_fatura.Tarifa = self.get_tarifa()

        return self.dados_fatura

    def get_valor_faturado(self):
        return 100

    def get_valor_ajuste(self):
        return 60

    def get_tarifa(self):
        return 1.0586
