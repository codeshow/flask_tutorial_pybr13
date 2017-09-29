# 1) Arquitetura do Projeto e dicas de estrutura e qualidade

Instalado através do `setup.py` com `python setup.py develop` e irá prover 
a ferramenta de linha de comando `cms` a partir da qual iremos rodar 
`cms runserver` e `cms shell` e `cms adduser`

A estrutura do projeto será:

```bash
Makefile               # Utilidades `install`, `clean`, `pep8` e `test`
setup.py               # Instalador do projeto `python setup.py develop`
tests/                 # Testes com py.test
cms/                   # module root
├── app/               # Application Factory (Flask app será iniciada aqui)
├── config/            # Configuration Factory (Load de configurações)
├── ext/               # Extensões (Blueprints) do app
├── static/            # Arquivos estáticos (.css, .js, .images)
├── templates/         # Templates Jinja2
├── cli.py             # Ferramenta de linha de comando `cms --help`
├── __init__.py        # Python module init
├── README.md          # Este arquivo
└── settings.yml       # Configurações que serão carregadas
```
