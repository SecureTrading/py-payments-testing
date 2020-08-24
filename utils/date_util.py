from datetime import datetime, timedelta

from attrdict import AttrDict


def get_current_time():
    return datetime.now()


# easily this whole class could be extended
# e.g. adjust date by minutes/hours etc.
def adjust_date_day(original_date, offset):
    return original_date + timedelta(days=offset)


def convert_to_string(original_date, string_format):
    return original_date.strftime(string_format)


def convert_from_string(original_date, string_format):
    return datetime.strptime(original_date, string_format)


date_formats = AttrDict({
    'day_month_year': "%d.%m.%Y",
    'day_month_year_hour_minute': "%d.%m.%Y %H:%M",
    'day_month_year_hour_minute_second': "%Y-%m-%d %H:%M:%S",
    'month_year': "%m/%y"
})
