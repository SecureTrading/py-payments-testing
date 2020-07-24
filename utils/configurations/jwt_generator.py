import time
import jwt
import json
import os

JWT_JSON_CONFIG_FILES_BESEDIR = os.path.abspath('jwt_config_files')

SECRET_KEY = os.environ.get('SECRET_KEY')


def get_data_from_json(jwt_config):
    with open(JWT_JSON_CONFIG_FILES_BESEDIR + f'/{jwt_config}', 'r') as file:
        jwt_json = json.load(file)
    return jwt_json


def encode_jwt_for_json(json_config, secret):
    data = get_data_from_json(json_config)
    return jwt.encode({"iat": int(time.time()), "iss": data["iss"], "payload": data["payload"]}, secret, algorithm='HS256')


