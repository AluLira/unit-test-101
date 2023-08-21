import os

import pytest

from unit_tests_101.dto.s3_record_dto import S3RecordDTO


def _create_local_response(test_dir, test_file):
    file_name = f"{test_dir}/pdf/{test_file}"
    with open(file_name, "r", encoding="utf-8") as file:
        data = file.read()

    return bytes(data, "utf-8")


@pytest.fixture(scope="module")
def builder_configuration():
    # Assert
    def _get_builder_configuration(
        current_location, test_file, builder, s3_record=None
    ):
        os.environ["RDS_DB_CONN_STRING"] = "TestDBConnStr"
        fatura_data = _create_local_response(
            test_dir=current_location, test_file=test_file
        )

        builder = builder(s3_record, fatura_data)
        builder.build_response()
        return builder

    return _get_builder_configuration


@pytest.fixture()
def s3_record():
    return S3RecordDTO(
        {
            "bucket": "test-bucket",
            "object": "test/object_id",
            "modification_date": "2023/08/08",
        }
    )
