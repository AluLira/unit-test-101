import os

from unit_tests_101.utils.aws_utils import AWSUtils


class TestingManager(object):
    def __init__(self):
        self.connection_string = AWSUtils.get_parameter_ssm(
            os.environ["RDS_DB_CONN_STRING"]
        )
