# Use a imagem oficial do Python 3.10 como base
FROM python:3.10-slim

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Instale o nltk e baixe o recurso vader_lexicon
RUN python -c "import nltk; nltk.download('vader_lexicon')"

# Copie o conteúdo do diretório local para o diretório de trabalho do contêiner
COPY ./api api

# Expõe a porta 8000 para acesso externo
EXPOSE 8000

# Comando para iniciar a aplicação FastAPI usando uvicorn
CMD ["uvicorn", "api.main:api", "--host", "0.0.0.0", "--port", "8000"]
