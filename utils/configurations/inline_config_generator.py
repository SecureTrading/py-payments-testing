import json

from utils.enums.e2e_config import e2eConfig


def get_data_from_json(e2e_config):
    with open('wiremock/__files/e2e_config' + f'/{e2e_config}', 'r') as file:
        jwt_json = json.load(file)
    return jwt_json


def covert_json_to_string(json_config):
    inline_config = "inlineConfig=" + json.dumps(json_config)
    formatted_config = inline_config.replace(" ", "")
    return formatted_config


def create_inline_config(e2e_config: e2eConfig, jwt):
    json_config = get_data_from_json(e2e_config.value)
    json_config["jwt"] = jwt.decode('UTF-8')
    formatted_config = covert_json_to_string(json_config)
    return formatted_config