import os
from dotenv import load_dotenv


load_dotenv()

# Obtenha a chave secreta do arquivo da variável de ambiente
secret_key = os.getenv("SECRET_KEY")
