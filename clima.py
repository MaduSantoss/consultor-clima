import requests
from dotenv import load_dotenv
import os

# Carrega o arquivo .env
load_dotenv()

API_KEY = os.getenv("API_KEY")

cidade = input("Digite o nome da cidade: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(url)

dados = requisicao.json()

if dados['cod'] != 200:
    print("Cidade não encontrada ou erro na conexão.")
else:
    # Pegando a descrição do clima
    descricao = dados['weather'][0]['description']

    # Pegando a temperatura em Kelvin e convertendo para Celsius
    temp_kelvin = dados['main']['temp']
    temp_celsius = temp_kelvin - 273.15

    print(f"\n🌍 Clima em {cidade}: {descricao}")
    print(f"🌡️  Temperatura: {temp_celsius:.1f}°C")