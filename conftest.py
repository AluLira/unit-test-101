import pytest


def _create_local_response(test_dir, test_file):
    file_name = f"{test_dir}/html/{test_file}"
    with open(file_name, "r", encoding="utf-8") as file:
        data = file.read()

    return bytes(data, "utf-8")

@pytest.fixture(scope="module")
def builder_configuration():
    # Assert
    def _get_builder_configuration(
            current_location, test_file, builder
    ):
        fatura_data = _create_local_response(
            test_dir=current_location, test_file=test_file
        )

        builder = builder()
        builder.build_response()
        return builder

