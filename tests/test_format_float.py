from time import time
from base64 import b64encode
from freezegun import freeze_time
from src.format_float import is_valid_header


@freeze_time("2019-07-23 20:20:34.25")
def test_valid_header():
    seconds_since_epoch = time()  # Return the time in seconds since the epoch as a floating point number
    header_timestamp = '{:.2f}'.format(seconds_since_epoch)
    timestamp_bytes = bytes(header_timestamp, 'utf-8')
    encoded_header = b64encode(timestamp_bytes)

    assert is_valid_header(encoded_header) is True
