from dotenv import load_dotenv
from pathlib import Path
import os

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
    root_dir = Path('.').resolve().parent
    config_dir = root_dir / Path('etc') / Path('config')
    print(config_dir)
    if dir_exists(config_dir):
        return config_dir
    else:
        return None


def dir_exists(directory_path):
    return os.path.exists(directory_path)


def file_exists(file_path):
    return os.path.isfile(file_path) or Path(str(file_path)).is_file()


def get_config_abs_path():
    config_dir = get_config_dir()
    if not config_dir:
        raise Exception('config directory not found')
    config_file_name = get_config_file_name()
    env_file_path = config_dir / Path(config_file_name)

    if not file_exists(env_file_path):
        raise Exception('environment file not found')

    return env_file_path


# Get absolute path to the config file
env_path = get_config_abs_path()
# Load the environment variables
load_dotenv(dotenv_path=env_path)
