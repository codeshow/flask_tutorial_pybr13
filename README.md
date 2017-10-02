# Tutorial Flask Python Brasil 13

Aprenda Flask criando um CMS e suas extensões

## Objetivos

Tutorial mão na massa onde os participantes irão aprender a configurar a
arquitetar um aplicativo Flask para gestão de conteúdo (BLOG, Site, Portal etc)

### CMS?

CMS é Content Management System, é o nome a qualquer sistema que permita gerenciamento
dinâmico de conteúdo e a apresentação e controle de seu acesso.

Serve para criarção de blogs, sites, portais etc.. (ex: Quokka CMS, Django CMS, Wordpress)

## Tópicos

- **Flask 101**  
    (teórico + demos ~ 1h `periodo da manhã`)

    * Hello world e o ambiente `web`
    * App e configurações
    * Views e Rotas
    * Responses
    * Requests
    * session
    * Templates
    * Extensões

- **Arquitetura e boas práticas**  
    (teórico + demo ~ 1h `periodo da manhã`)

    * `12 factor`: configurações dinâmicas
    * The Factory pattern  
      (evitando problemas com circular imports)
    * Extensões e blueprints  
      (criando módulos/plugins reusaveis)
    * Testing
    * Servindo a app

- **Construindo o CMS**  
    (Prática - Mão na Massa - step by step ~4hrs `periodo da tarde`)
    * Arquitetura do Projeto e dicas de estrutura e qualidade - [Branch](../../tree/cms/cms)
    * CLI (tudo começa na linha de comando) - [Branch](../../tree/cms_2_cli/cms)
    * Factories
        * Application factory - [Branch](../../tree/cms_3_app_factory/cms)
        * Configuration factory - [Branch](../../tree/cms_3_config_factory/cms)
        * Extension factory - [Branch](../../tree/cms_3_extension_factory/cms)
            * Autenticação
            * Banco de dados NoSQL  
              (neste tutorial não abordaremos SQL nem ORMs)
    * Flask-Admin, AdminViews & WTForms - [Branch](../../tree/cms_4_blog/cms)
    * Jinja - [Branch](../../tree/cms_5_jinja/cms)
    * Jinja Extensions - [Branch](../../tree/cms_5_template_globals/cms)
    * Arquivos estáticos - [Branch](../../tree/cms_6_static/cms)
    * WSGI - [Branch](../../tree/cms_7_wsgi/cms)
    * test - [Branch](../../tree/cms_8_test/cms)

## Requisitos


### Parte 1 - manhã

Para participar da parte teórica (periodo da manhã) não tem nenhum requisito, todas as pessoas de qualquer nivel de conhecimento mesmo sem um computador pode participar.


### parte 2 - tarde


#### Conhecimento 

Para a parte prática é necessário conhecimento básico iniciante em `Python`, o foco será na explicação das funcionalidade do `Flask` e não serão explicados conceitos da linguagem como por exemplo o que são classes, funções, métodos, decorators, módulos etc..

Contudo será apresentado snippets de código para serem replicados portanto não é necessário entendimento complexo de Python para conseguir participar.

#### Técnicos

* Computador com `Python 3.6+` instalado, não será abordado a instalação do Python3.6 portanto aconselho estar com esta versão já disponivel.
(recomendo a ferramenta `pyenv` para automatizar a instalação e aproveite os dias que antecedem o tutorial para conseguir ajuda durante o evento para instalar)

* Sistema operacional de sua preferencia desde que tenha dominio do uso de seu `console/terminal`, recomendo o uso de **Linux**

* Editor de códigos de sua preferencia, não será preciso funcionalidades avançadas de IDEs, portanto qualquer editor básico é suficiente. 
(recomendo: Gedit, Notepad++, Sublime, Atom, VSCode, Vim)

* Browser atualizado (Chrome ou Firefox)

* Se tiver acesso a internet no local do tutorial será excelente para instalar as dependencias. Porém recomendo clonar este repositório:

Preparando o ambiente e instalando as dependencias (faça isso antes do dia do tutorial em um local com acesso a internet)

```bash
git clone git@github.com:cursodepythonoficial/flask_tutorial_pybr13.git flask_pybr
cd flask_pybr
python3.6 -m venv venv
. venv/bin/activate
cd cms
venv/bin/pip3 install requirements.txt  
```

* Opcionalmente pode baixar este [zip](https://github.com/cursodepythonoficial/flask_tutorial_pybr13/raw/master/files/env.tgz) que já contém todas as dependencias e exemplos de código.


## Advanced

Se você quiser clonar de uma só vez todas as branches deste repositório execute:

```bash
mkdir flask_pybr;cd flask_pybr;git clone --bare git@github.com:cursodepythonoficial/flask_tutorial_pybr13.git .git;git config --unset core.bare;git reset --hard

# agora pode mudar para a ultima branch (projeto completo)
git checkout cms_8_test
pip install -r requirements.txt
python setup.py install
cms adduser
cms runserver
```

## Info

- Data: 09/10
- Horário: 8:30 (é bom chegar mais cedo também!)
- Local: UNA Barro Preto (https://goo.gl/maps/82tiKzTvMzC2)
- Detalhes: http://2017.pythonbrasil.org.br/#schedule
- Inscrição: Tutoriais são treinamentos de 3 a 6 horas totalmente gratuitos para você se tornar um Jedi. A menos que informado do contrário, a entrada aos tutoriais são abertas, por ordem de chegada, sem necessidade de inscrição.

## Contatos

Bruno Rocha - [@rochacbruno](http://github.com/rochacbruno)

http://about.me/rochacbruno

http://brunorocha.org


---


![CursoDePython](https://avatars2.githubusercontent.com/u/31020499?v=4&s=200)

- http://facebook.com/CursoDePython
- http://Youtube.com/CursoDePython
- http://plus.google.com/+CursoDePython
- http://cursodepython.com.br
- https://github.com/cursodepythonoficial

Guarulhos São Paulo - BR

### Conteúdo sob Licença

Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
