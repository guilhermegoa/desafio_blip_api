# Nome do Projeto

O Desafio Técnico consiste na criação de um microserviço RESTful utilizando o framework FastAPI em Python. Este microserviço deve receber texto como entrada e retornar informações processadas utilizando um modelo de Processamento de Linguagem Natural (NLP). Para a realização deste desafio, você pode utilizar o modelo de tokenização de palavras da biblioteca NLTK ou outro modelo de NLP de sua escolha.

[Arquivo de teste](docs/desafio-tcnico-se-_-jorel.pdf)

## Estrutura de Arquivos

Aqui está a estrutura de arquivos básica do projeto:

```txt
    desafio_blip_api/
    │
    ├── api/
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
    ├── api.py
    ├── requirements.txt
    ├── README.md
    └── .gitignore
```

## Descrição dos Arquivos

- **`api/`**: Este diretório contém os componentes da API.
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
      - **`analyser_test.py`**: Arquivo que define os testes para o serviço de análise.
      - **`__init__.py`**: Arquivo de inicialização do pacote de testes de serviço.
  - **`__init__.py`**: Arquivo de inicialização do pacote api.
  - **`main.py`**: Arquivo principal que contém a lógica principal da API.

- **`api.py`**: Script principal para executar a API.
- **`requirements.txt`**: Arquivo que lista todas as dependências do projeto e suas versões para instalação com pip.
- **`README.md`**: Arquivo de readme que contém informações sobre o projeto.
- **`.gitignore`**: Arquivo que especifica arquivos e diretórios que devem ser ignorados pelo controle de versão Git.

## Instalação

Para instalar as dependências do projeto, você pode utilizar o gerenciador de pacotes Python, pip. Certifique-se de ter o Python instalado em seu sistema antes de prosseguir.

```cmd
    python -m pip install -r requirements.txt
```

Certifique-se de estar no diretório raiz do projeto ao executar este comando. Isso instalará todas as dependências listadas no arquivo requirements.txt em seu ambiente Python.

## Executar

Para executar em modo de recarga automática:

```cmd
    uvicorn.exe api.main:api --reload
```

Para executar em modo de recarga automática:

```cmd
    python api.py
```

Certifique-se de estar no diretório correto do projeto ao executar esses comandos. O primeiro comando usa o Uvicorn para executar o aplicativo FastAPI em modo de desenvolvimento com recarga automática, enquanto o segundo comando executa o aplicativo em produção sem recarga automática.