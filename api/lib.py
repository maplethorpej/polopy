import datetime

range_periods = {
    'LAST_HOUR': {
        'period': 300,
        'seconds': 60 * 60
    },
    'LAST_DAY': {
        'period': 900,
        'seconds': 60 * 60 * 24
    },
    'LAST_WEEK': {
        'period': 1800,
        'seconds': 60 * 60 * 24 * 7
    },
    'LAST_MONTH': {
        'period': 7200,
        'seconds': 60 * 60 * 24 * 30
    },
    'LAST_YEAR': {
        'period': 36000,
        'seconds': 60 * 60 * 24 * 365
    },
    'ALL_TIME': {
        'period': 86400,
        'seconds': 60 * 60 * 24 * 365 * 20  # twenty years
    }
}


class TimeRange:
    def __init__(self, time_range):
        self.range = time_range
        self.utc_now = datetime.datetime.utcnow()

    @property
    def get(self):
        time_range = range_periods[self.range]

        # convert to unix timestamp
        start = self.utc_now.timestamp()
        end = (self.utc_now - datetime.timedelta(seconds=time_range['seconds'])).timestamp()
        period = time_range['period']

        return {
            'start': start,
            'end': end,
            'period': period
        }
