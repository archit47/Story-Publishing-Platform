from dotenv import load_dotenv
from pathlib import Path
import os
from utils import os_utils

# some environment constants
DEV = 'dev'
PROD = 'prod'
STAG = 'stag'


def get_environment():
    env_type = os.getenv('ENV')

    if (not env_type) or env_type.startswith('dev'):
        return DEV
    elif env_type.startswith('prod'):
        return PROD
    else:
        return STAG


def get_config_file_name():
    env = get_environment()
    env = env.strip()
    return '{}.env'.format(env)


def get_config_dir():
    # root_dir = Path('.').resolve().parent
    root_dir = Path('.').resolve()
    config_dir = root_dir / Path('etc') / Path('config')
    print(config_dir)
    if os_utils.directory_exists(config_dir):
        return config_dir
    else:
        return None


def get_config_abs_path():
    config_dir = get_config_dir()
    if not config_dir:
        raise Exception('config directory not found')
    config_file_name = get_config_file_name()
    env_file_path = config_dir / Path(config_file_name)

    if not os_utils.file_exists(env_file_path):
        raise Exception('environment file not found')

    return env_file_path


# Get absolute path to the config file
env_path = get_config_abs_path()
print(env_path)
# Load the environment variables
load_dotenv(dotenv_path=env_path)
