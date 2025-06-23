# Usa uma imagem base oficial do Python para garantir o ambiente necessário
FROM python:3.9-slim-buster

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos da aplicação para o diretório de trabalho
COPY . .

# Define o comando para executar o bot quando o container for iniciado
CMD ["python", "bot.py"]
