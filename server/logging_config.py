import logging
import os
from dotenv import load_dotenv


base_path = os.path.dirname(__file__)

for filename in ['.env', '.env.local']:
    env_file = os.path.join(base_path, filename)
    if os.path.exists(env_file):
        load_dotenv(env_file, override=(filename == '.env.local'))


debug_mode = os.getenv("DEBUG", "False").lower() == "true"

log_dir = os.getenv("LOG_DIR", os.path.dirname(__file__))
# os.makedirs(log_dir, exist_ok=True)

def setup_logging():
    log_filename = os.path.join(log_dir, "storapi.log")

    handler = logging.FileHandler(log_filename)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter( "%(asctime)s - %(message)s" ))

    logger = logging.getLogger("velziapi")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    if not logger.hasHandlers():
        logger.addHandler(handler)

    return logger


def close_loggers(logger):
    handlers = logger.handlers[:]
    for handler in handlers:
        handler.flush()
        handler.close()
        logger.removeHandler(handler)


def get_logger():
    logger = logging.getLogger("velziapi")
    if not logger.hasHandlers():
        setup_logging()
    return logger
