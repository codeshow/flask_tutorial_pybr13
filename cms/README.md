Neste diretório o projeto de CMS será desenvolvido, mão na massa! é com você

# 0) Prepare seu ambiente

Você vai precisar de:

- Python 3.6+
- Editor de códigos de sua preferencia
- Navegador Web

> NOTA: para instalar o Python3.6 será necessário ter a zlib, no ubuntu instala-se com `sudo apt-get install zlib1g-dev` e no fedora/red-hat é `sudo yum install zlib-devel` procure como instalar a zlib no seu sistema operacional.


## Windows?

Se estiver usando windows baixe o instalador do Python 3.6 no site oficial http://python.org

## Instale o Python 3.6

Digite `python3 -V` no seu console, caso a versão seja menor que `3.6` você precisará instalar e para isso recomendo usar o `pyenv` e tem um tutorial bem legal neste [link](http://blog.abraseucodigo.com.br/instalando-qualquer-versao-do-python-no-linux-macosx-utilizando-pyenv.html)

## Prepare sua VirtualEnv

Crie uma pasta para o projeto e dentro dela faça o clone deste repositório e crie a virtualenv

```bash
git clone https://github.com/cursodepythonoficial/flask_tutorial_pybr13.git flask_pybr
cd flask_pybr
python3.6 -m venv venv
. venv/bin/activate
```

## Instale as dependências

```bash
venv/bin/pip3 install -r requirements.txt
```

[próximo -->>](../../../tree/cms/cms)
