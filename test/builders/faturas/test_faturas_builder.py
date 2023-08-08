from pathlib import Path

import pytest

from unit_tests_101.dto.s3_record_dto import S3RecordDTO
from unit_tests_101.data_model.models.fatura_model import Fatura
from unit_tests_101.data_model.builder.faturas_builder import FaturaBuilder


@pytest.fixture(scope="module")
def builder(builder_configuration):
    parent_dir = Path(__file__).parent
    base_builder = FaturaBuilder
    s3_record = S3RecordDTO(
        {
            "bucket": "test-bucket",
            "object": "test/object_id",
            "modification_date": "2023/08/08",
        }
    )

    builder = builder_configuration(
        current_location=parent_dir,
        test_file="pdf_fatura.html",
        builder=base_builder,
        s3_record=s3_record,
    )
    yield builder


def test_valores_fatura(builder: FaturaBuilder, mocker):
    aws_call = mocker.patch("unit_tests_101.utils.aws_utils.AWSUtils.salvar_dados_rds")

    retorno_fatura = builder.build_response()

    assert isinstance(retorno_fatura, Fatura)

    assert builder.dados_fatura.Faturado == 100
    assert builder.dados_fatura.Ajuste == 60
    assert builder.dados_fatura.Tarifa == 1.0586

    assert aws_call.call_count == 1
