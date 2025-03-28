import os
import random
import traceback
from dotenv import load_dotenv

base_path = os.path.dirname(__file__)

for filename in ['.env', '.env.local']:
    env_file = os.path.join(base_path, filename)
    if os.path.exists(env_file):
        load_dotenv(env_file, override=(filename == '.env.local'))

OBFUSCATE_KEYS = os.getenv("KEYS_TO_OBFUSCATE", "").split(",")


def get_line_number():
    stack = traceback.format_stack()
    info = stack[-2].strip().split('\n')[0].replace("File ", "").strip().replace('"', '').split(', ')

    return f"{info[0]} {info[2]}: {info[1]}"


def mask_sensitive_data(token):
    return f"{'*' * random.randint(5, 20)}{token[-4:] if token else ''}"


def obfuscate_headers(request_headers):
    headers = {
        k: (mask_sensitive_data(v) if any(key.lower() in k.lower() for key in OBFUSCATE_KEYS) else v)
        for k, v in request_headers.items()
    }
    return headers
