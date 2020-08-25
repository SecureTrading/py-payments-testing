import time
import json
import os

import jwt

from utils.enums.jwt_config import JwtConfig

SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'you_will_never_guess'
ISS_KEY = os.environ.get('JWT_ISS_KEY') or 'you_will_never_guess'


def get_data_from_json(jwt_config):
    with open('utils/configurations/jwt_config_files' + f'/{jwt_config}', 'r') as file:
        jwt_json = json.load(file)
    return jwt_json


def encode_jwt_for_json(jwt_config: JwtConfig):
    data = get_data_from_json(jwt_config.value)
    jwt_token = jwt.encode({"iat": int(time.time()), "iss": ISS_KEY, "payload": data["payload"]}, SECRET_KEY, algorithm='HS256')
    return str(jwt_token, "utf-8")