from pathlib import Path

import pytest

from unit_tests_101.data_model.builder.faturas_builder import (
    FaturaBuilder
)


@pytest.fixture(scope="module")
def builder(builder_configuration):
    parent_dir = Path(__file__).parent
    base_builder = FaturaBuilder

    builder = builder_configuration(
        current_dir=parent_dir,
        test_file="pdf_fatura.html",
        builder=base_builder,
    )
    yield builder

