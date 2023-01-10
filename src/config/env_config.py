import os
from dotenv import load_dotenv

load_dotenv()

env = {
    "POSTGRES_DB": os.getenv('POSTGRES_DB'),
    "DATABASE_URL": os.getenv('DATABASE_URL'),
    "POSTGRES_USER": os.getenv('POSTGRES_USER'),
    "POSTGRES_PASSWORD": os.getenv('POSTGRES_PASSWORD')
}

# print(env.get("POSTGRES_DB"))


def to_recover_env():
    """Função que retorna as variáveis de ambientes"""
    return env


# print(to_recover_env())
