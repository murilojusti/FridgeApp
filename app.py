from dotenv import load_dotenv
import os
import openai

# Carregar variáveis do arquivo .env
load_dotenv()

# Pegar a API Key
openai.api_key = os.getenv("sk")