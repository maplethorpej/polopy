import time
import math
from urllib.parse import urlencode

range_periods = {
    'LAST_HOUR': {
        'period': 300,
        'seconds': 60 * 60,
        'expires': 60 * 5
    },
    'LAST_DAY': {
        'period': 900,
        'seconds': 60 * 60 * 24,
        'expires': 60 * 30
    },
    'LAST_WEEK': {
        'period': 1800,
        'seconds': 60 * 60 * 24 * 7,
        'expires': 60 * 60 * 6
    },
    'LAST_MONTH': {
        'period': 7200,
        'seconds': 60 * 60 * 24 * 30,
        'expires': 60 * 60 * 12
    },
    'LAST_YEAR': {
        'period': 14400,
        'seconds': 60 * 60 * 24 * 365,
        'expires': 60 * 60 * 48
    },
    'ALL_TIME': {
        'period': 86400,
        'seconds': 60 * 60 * 24 * 365 * 20,  # twenty years,
        'expires': 60 * 60 * 48
    }
}


class TimeRange:
    def __init__(self, time_range):
        self.range = time_range
        self.unix_timestamp = time.time()

    @property
    def get_query_str(self):
        time_range = range_periods[self.range]

        # convert to unix timestamp
        start = math.floor(self.unix_timestamp) - time_range['seconds']
        end = math.floor(self.unix_timestamp)
        period = time_range['period']

        query = {
            'start': start,
            'end': end,
            'period': period
        }

        return urlencode(query)
