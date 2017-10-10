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

Para criar os arquivos iniciais execute as 2 linhas abaixo

```bash
mkdir -p tests cms/{app,config,ext,static,templates}
touch cms/{cli.py,__init__.py,settings.yml,{app,config,ext}/__init__.py}
```

No `setup.py` temos a seguinte configuração:

```python
setup(
    name='cms',
    version='0.0.1',
    description="A simple CMS in Flask",
    packages=['cms'],
    package_dir={'cms': 'cms'},
    entry_points={
        'console_scripts': [
            'cms=cms.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements
)

```

agora ao rodar `python setup.py develop` a ferramente `cms` estará disponível.


O app será servido ao digitar `cms runserver` na linha de comando

```bash
cms runserver
``` 

Porém como ainda não escrevemos a implementação de `cli.py` este código irá falhar

```bash
ImportError: module 'cms.cli' has no attribute 'main'
```

Portanto precisamos implementar a função `main` no módulo `cli.py`


[<<-- anterior](../../../tree/master/cms)  -  [próximo -->>](../../../tree/cms_2_cli/cms)
