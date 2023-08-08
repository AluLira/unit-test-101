import gzip
import os
import time
import uuid
import boto3
import json

from botocore.exceptions import ClientError


class AWSUtils:
    @staticmethod
    def get_parameter_ssm(parameter_name, encrypted=False):
        """Função para pegar parametro especifico no ssm"""
        pass

    @staticmethod
    def upload_content_to_s3(content, bucket, object_name=None, gzipped=True):
        """Função para enviar arquivos para o s3"""
        pass

    @staticmethod
    def send_sqs_message(url, message_body, message_attributes, region="us-east-1"):
        """Função para enviar mensagens para uma fila SQS"""
        pass
