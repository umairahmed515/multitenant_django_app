import json
import os
from typing import Any

from django.core.exceptions import ImproperlyConfigured

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))

ENV = os.environ.get("env")

try:
    config_file_path = ""
    if ENV == "local":
        config_file_path = os.path.join(PROJECT_PATH, "settings/local_config.json")
    if not config_file_path:
        raise FileNotFoundError(
            f"Configuration File Path Not Found For Environment: ${ENV}"
        )
    with open(config_file_path) as config_file:
        configs = json.loads(config_file.read())
except Exception:
    raise FileNotFoundError(
        f"Improperly configured environment variable. Environment: ${ENV}"
    )


def get_env_var(setting: Any, configurations=configs, default=None):
    try:
        val = configurations[setting]
        if val == "True":
            val = True
        elif val == "False":
            val = False
        return val
    except KeyError:
        if default is not None:
            return default
        error_msg = f"ImproperlyConfigured: Set {setting} environment variable."
        raise ImproperlyConfigured(error_msg)


DATABASE_ENGINE = get_env_var("DATABASE_ENGINE")
DATABASE_USER = get_env_var("DATABASE_USER")
DATABASE_PASSWORD = get_env_var("DATABASE_PASSWORD")
DATABASE_NAME = get_env_var("DATABASE_NAME")
DATABASE_HOST = get_env_var("DATABASE_HOST")
DATABASE_PORT = get_env_var("DATABASE_PORT")
