from unit_tests_101.dto.s3_record_dto import S3RecordDTO

from unit_tests_101.managers.testing_manager import TestingManager

from unit_tests_101.utils.aws_utils import AWSUtils

from unit_tests_101.data_model.models.fatura_model import Fatura


class FaturaBuilder:
    def __init__(
            self,
            record: S3RecordDTO,
            s3_content: bytes,
    ):
        self.arquivo_fatura = record
        self.dados_fatura = Fatura()

    def build_response(self):
        self.dados_fatura.Faturado = self.get_valor_faturado()
        self.dados_fatura.Ajuste = self.get_valor_ajuste()
        self.dados_fatura.Tarifa = self.get_tarifa()

        self.salvar_no_db()

        return self.dados_fatura

    def get_valor_faturado(self):
        """Método para extrair valor faturado a partir do arquivo da fatura"""
        return 100

    def get_valor_ajuste(self):
        """Método para extrair valor do ajuste a partir do arquivo da fatura"""
        return 60

    def get_tarifa(self):
        """Método para extrair valor da tarifa a partir do arquivo da fatura"""
        return 1.0586

    # Para simplificar coloquei a função de salvar os dados no RDS dentro do builder
    # mas a maneira correta de fazer chamadas para guardar objetos/dados ou
    # enviar mensagens (SQS/SNS) é dentro do use case da função Lambda.
    def salvar_no_db(self):
        """Método para salvar as informações da fatura no DB"""
        manager = TestingManager()
        AWSUtils.salvar_dados_rds(self.dados_fatura)
