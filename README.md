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

- Flask 101  
    (teórico + demos ~ 1h `periodo da manhã`)

    * Hello world e o ambiente `web`
    * App e configurações
    * Views e Rotas
    * Responses
    * Requests
    * session
    * Templates
    * Extensões

- Arquitetura e boas práticas  
    (teórico + demo ~ 1h `periodo da manhã`)

    * `12 factor`: configurações dinâmicas
    * The Factory pattern  
      (evitando problemas com circular imports)
    * Extensões e blueprints  
      (criando módulos/plugins reusaveis)
    * Testing
    * Servindo a app

- Construindo o CMS  
    (Prática - Mão na Massa - step by step ~4hrs `periodo da tarde`)
    * Arquitetura do Projeto e dicas de estrutura e qualidade
    * CLI (tudo começa na linha de comando)
    * Factories
        * Application factory
        * Configuration factory
        * Extension Factory
    * Autenticação
    * Banco de dados NoSQL  
      (neste tutorial não abordaremos SQL nem ORMs)
    * Flask-Admin, AdminViews & WTForms
    * Jinja environment & Extensions

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
