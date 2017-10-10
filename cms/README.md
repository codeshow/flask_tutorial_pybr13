Neste diretório o projeto de CMS será desenvolvido, mão na massa! é com você

# 0) Prepare seu ambiente

Você vai precisar de:

- Python 3.6+
- Editor de códigos de sua preferencia
- Navegador Web


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
