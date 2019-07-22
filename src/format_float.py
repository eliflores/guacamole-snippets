from base64 import b64decode
from time import time


def is_expired_header(timestamp):
    return time() - timestamp > 60


def is_valid_header(header):
    decoded_header = b64decode(header)
    header_timestamp = float(decoded_header)

    if is_expired_header(header_timestamp):
        return False

    client_timestamp = str(decoded_header, 'utf-8')
    server_timestamp = str(header_timestamp)

    return client_timestamp == server_timestamp
