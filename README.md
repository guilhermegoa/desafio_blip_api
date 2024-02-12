# Desafio Blip

O Desafio Técnico consiste na criação de um microserviço RESTful utilizando o framework FastAPI em Python. Este microserviço deve receber texto como entrada e retornar informações processadas utilizando um modelo de Processamento de Linguagem Natural (NLP). Para a realização deste desafio, você pode utilizar o modelo de tokenização de palavras da biblioteca NLTK ou outro modelo de NLP de sua escolha.

[Arquivo de teste](docs/desafio-tcnico-se-_-jorel.pdf)

## Estrutura de Arquivos

Aqui está a estrutura de arquivos básica do projeto:

```txt
  desafio_blip_api/
  │
  ├── app/
  │   ├── configurations/
  │   │   ├── __init__.py
  │   │   ├── exceptions/
  │   │   │   ├── __init__.py
  │   │   │   ├── exceptions_default_handler.py
  │   │   │   └── sentiment_analyze_exception.py
  │   │   └── validations/
  │   │       ├── __init__.py
  │   │       ├── str_validation.py
  │   │       └── word_validation.py
  │   ├── models/
  │   │   ├── __init__.py
  │   │   └── analyzer_model.py
  │   ├── routers/
  │   │   ├── __init__.py
  │   │   └── analyzer_router.py
  │   ├── services/
  │   │   ├── __init__.py
  │   │   └── analyzer_service.py
  │   ├── teste/
  │   │   ├── __init__.py
  │   │   └── services/
  │   │       ├── __init__.py
  │   │       └── analyzer_test.py
  │   ├── __init__.py
  │   └── main.py
  │
  ├── my_app.py
  ├── requirements.txt
  ├── README.md
  ├── Dockerfile
  ├── docker-compose.yml
  └── .gitignore
```

## Descrição dos Arquivos

- **`app/`**: Este diretório contém os componentes da API.
- **`configurations/`**: Contém configurações do aplicativo.
  - **`__init__.py`**: Arquivo de inicialização do pacote de configurações.
  - **`exceptions/`**: Diretório que contém as exceções personalizadas do aplicativo.
    - **`__init__.py`**: Arquivo de inicialização do pacote de exceções.
    - **`exceptions_default_handler.py`**: Arquivo que define o manipulador de exceções padrão.
    - **`sentiment_analyze_exception.py`**: Arquivo que define a exceção `SentimentAnalyzeException`.
  - **`validations/`**: Diretório que contém as validações personalizadas do aplicativo.
    - **`__init__.py`**: Arquivo de inicialização do pacote de validações.
    - **`str_validation.py`**: Arquivo que define validações para strings.
    - **`word_validation.py`**: Arquivo que define validações para palavras.
- **`models/`**: Contém os modelos de dados da API.
  - **`__init__.py`**: Arquivo de inicialização do pacote models.
  - **`analyzer.py`**: Arquivo que define os modelos de dados para análise.
- **`routers/`**: Contém os roteadores da API.
  - **`__init__.py`**: Arquivo de inicialização do pacote routers.
  - **`analyzer.py`**: Arquivo que define os roteadores para análise.
- **`services/`**: Contém os serviços da API.
  - **`__init__.py`**: Arquivo de inicialização do pacote services.
  - **`analyzer.py`**: Arquivo que define os serviços para análise.
- **`teste/`**: Contém os testes da API.
  - **`__init__.py`**: Arquivo de inicialização do pacote teste.
  - **`services/`**: Contém os testes de serviço.
    - **`analyzer_test.py`**: Arquivo que define os testes para o serviço de análise.
    - **`__init__.py`**: Arquivo de inicialização do pacote de testes de serviço.
- **`__init__.py`**: Arquivo de inicialização do pacote api.
- **`main.py`**: Arquivo principal que contém a lógica principal da API.

- **`my_app.py`**: Script principal para executar a API.
- **`requirements.txt`**: Arquivo que lista todas as dependências do projeto e suas versões para instalação com pip.
- **`README.md`**: Arquivo de readme que contém informações sobre o projeto.
- **`Dockerfile`**: Arquivo de configuração do Docker que define como as imagens Docker são construídas.
- **`docker-compose.yml`**: Arquivo de configuração do Docker Compose que define a execução de aplicativos Docker multi-container.
- **`.gitignore`**: Arquivo que especifica arquivos e diretórios que devem ser ignorados pelo controle de versão Git.

## Instalação

Para instalar as dependências do projeto, você pode utilizar o gerenciador de pacotes Python, pip. Certifique-se de ter o Python instalado em seu sistema antes de prosseguir.

```cmd
    python -m pip install -r requirements.txt
```

Certifique-se de estar no diretório raiz do projeto ao executar este comando. Isso instalará todas as dependências listadas no arquivo requirements.txt em seu ambiente Python.

## Executar

Primeiro rode o comando para fazer download.

```cmd
    python -c "import nltk; nltk.download('vader_lexicon')"
    python -c "import nltk; nltk.download('words')"
    python -c "import nltk; nltk.download('averaged_perceptron_tagger')"
```

Para executar em modo de recarga automática:

```cmd
    uvicorn.exe app.main:app --reload
```

Para executar sem modo de recarga automática:

```cmd
    python api.py
```

Certifique-se de estar no diretório correto do projeto ao executar esses comandos. O primeiro comando usa o Uvicorn para executar o aplicativo FastAPI em modo de desenvolvimento com recarga automática, enquanto o segundo comando executa o aplicativo em produção sem recarga automática.
