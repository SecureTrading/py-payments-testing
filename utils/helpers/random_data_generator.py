# pylint: disable=W,C,R
"""Separate module for random data generation. It is NOT being used
in basic framework configuration"""

import os
import ast
import json
import random
import string

from base64 import b16encode, b32encode, b64encode
from datetime import datetime, timedelta
from faker import Factory
from lxml import etree

DEFAULT_DATETIME_FORMAT = '%Y_%m_%d_%H_%M_%S'


class TestDataGenerator:
    _ttypes = {
        'int': int,
        'str': str,
        'float': float,
        'bool': ast.literal_eval,
        'list': ast.literal_eval
    }
    _encoders = {
        'base16': b16encode,
        'base32': b32encode,
        'base64': b64encode,
    }

    def __init__(self, external_files_path=None):
        self._external_files_path = external_files_path

    def generate(self, data_to_generate, constants_data=None):
        if isinstance(data_to_generate, dict):
            dict_type = type(data_to_generate)
            result = ((self.generate(k, constants_data),
                       self.generate(v, constants_data)) for k, v in
                      data_to_generate.items())
            return dict_type(result)

        elif isinstance(data_to_generate, list):
            result = [self.generate(dp, constants_data) for dp in data_to_generate]
            return result

        elif not isinstance(data_to_generate, str):
            return data_to_generate

        else:
            return self._generate(data_to_generate, constants_data)

    def _generate(self, data_to_generate, constants_data):
        if data_to_generate.startswith('constant#'):
            prefix, data_key = data_to_generate.split('#')
            data_to_generate = constants_data[data_key]['value']
        if data_to_generate.startswith(('random#', 'unique#')):
            prefix, value_parameter, *params = data_to_generate.split('#')
            if value_parameter in ['dict', 'json']:
                params = [5, True, 'str']
            generated_value = fake_data_generator(value_parameter, *params)
            if prefix == 'unique':
                generated_value = '%s%s' % (get_date_formatted('%Y%m%d%H%M%S'), generated_value)
            if value_parameter == 'json':
                generated_value = json.dumps(generated_value)
            return generated_value

        elif data_to_generate.startswith('string#'):
            prefix, *params = data_to_generate.split('#')
            params = [int(param) for param in params]
            return get_string(*params)

        elif data_to_generate.startswith('date_with_offset#'):
            prefix, *date_params = data_to_generate.split('#')
            date_formatted = get_date_with_offset_formatted(*date_params)
            return date_formatted

        elif data_to_generate.startswith(('file#', 'fromfile#')):
            data_to_generate.split('#')
            prefix, *paths = data_to_generate.split('#')
            file_path = os.path.join(self._external_files_path, *paths)
            if prefix == 'file':
                return open(file_path, 'rb').read()
            else:
                with open(file_path) as f:
                    return f.read()

        elif data_to_generate.startswith('#null'):
            return None

        elif data_to_generate.startswith('type#'):

            prefix, data_type, value = data_to_generate.split('#')
            return self._ttypes[data_type](value)

        elif data_to_generate.startswith('encoded#'):
            prefix, encoder, value = data_to_generate.split('#')
            return self._encoders[encoder](value.encode()).decode()

        else:
            return data_to_generate


faker_locales = ('en_US', 'en_GB')


def get_date_formatted(format_date=DEFAULT_DATETIME_FORMAT, **date_options):
    if 'date_bound' in date_options.keys():
        temp_date = datetime.strptime(date_options['date_bound'], format_date)
        data_print = datetime(temp_date.year, temp_date.month, temp_date.day)
    else:
        data_print = datetime.utcnow()
    if 'date_random' in date_options.keys():
        days_offset = random.randint(1, 20000)
        if date_options['date_random'] == 'before':
            data_print = data_print - timedelta(days=days_offset)
        if date_options['date_random'] == 'after':
            data_print = data_print + timedelta(days=days_offset)
    data_formatted = str(data_print.strftime(format_date))
    return data_formatted


def get_date_with_offset_formatted(days=0, hours=0, seconds=0, format_date=DEFAULT_DATETIME_FORMAT):
    days = int(days)
    hours = int(hours)
    seconds = int(seconds)
    data_print = datetime.utcnow() + timedelta(days=days, hours=hours, seconds=seconds)
    data_print = str(data_print.strftime(format_date))
    return data_print


def get_string(length, words=1, chars=string.ascii_letters + string.digits):
    generated_string = ''.join(random.choice(chars) for _ in range(length))
    average_word_length = length // words
    word_step = average_word_length
    for word in range(words - 1):
        range_bounds = [word_step, word_step + random.randint
                        (average_word_length // -2, average_word_length // 2)]
        space_position = random.randint(min(range_bounds), max(range_bounds))
        generated_string = generated_string[:space_position] + ' ' \
                                                   + generated_string[space_position + 1:]
        word_step += average_word_length
    return generated_string


def fake_data_generator(generate_string_type, *args, **kwargs):
    faker_switcher = {
        'street': 'street_address',
        'integer': 'random_int',
        'json': 'pydict',
        'string': 'word',
        'uuid': 'uuid4',
        'username': 'user_name'
    }
    func_name = faker_switcher.get(generate_string_type, generate_string_type)
    string_locale = kwargs.get('locale', random.choice(faker_locales))
    a = Factory.create(string_locale)
    func = getattr(a, func_name)
    if args:
        args = [int(a[3:]) if type(a) is str and a.startswith('int') else a for a in args]
        return func(*args)
    else:
        return func()
