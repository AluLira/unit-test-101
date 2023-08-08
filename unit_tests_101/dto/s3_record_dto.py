class S3RecordDTO:
    def __init__(self, record_data: dict):
        self._bucket = record_data.get("bucket")
        self._object_value = record_data.get("object")
