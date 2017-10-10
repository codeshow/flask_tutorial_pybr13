# 9) Deploy on PythonAnywhere


1) Create or login to your account on www.pythonanywhere.com

em https://www.pythonanywhere.com/user/YOURUSER/webapps/

Crie um novo web app e escolha `Flask` e `Python3.6`

![step1](https://user-images.githubusercontent.com/458654/31103187-13112aba-a7ac-11e7-9a59-503bdac3db58.png)


2) Defina `/home/YOURUSER/repo/cms/wsgi.py` como o Path do app

![step2](https://user-images.githubusercontent.com/458654/31103186-1310d538-a7ac-11e7-80e2-6ca0451b7b8c.png)

3) Vá ao dashboard consoles e inicie um novo `bash` console

```bash
cd ~
# delete the existing `repo` with 
rm -rf repo
# Clone the new repo
git clone -b cms_9_deploy https://github.com/cursodepythonoficial/flask_tutorial_pybr13.git repo
#acesse
cd repo
# deploy
./deploy.sh
#wait...
```
![step3](https://user-images.githubusercontent.com/458654/31103181-12f5dbf2-a7ac-11e7-95e4-f58aaaf01c15.png)


4) Volte ao https://www.pythonanywhere.com/user/yourname/webapps/

- Configure sourcecode como `/home/YOURUSER/repo/cms`
- Configure workdir como `/home/YOURUSER/repo`
- **Não altere o  `WSGI config file`**
- Configure virtualenv to `/home/YOURUSER/repo/venv`

![step4](https://user-images.githubusercontent.com/458654/31103184-12f9f48a-a7ac-11e7-94e3-eec2b87799ca.png)

5) Reload the web app

![step5](https://user-images.githubusercontent.com/458654/31103183-12f91c90-a7ac-11e7-9e91-00a84fb431ae.png)


6) Access the YOURNAME.pythonanywhere.com e veja o app rodando

![step6](https://user-images.githubusercontent.com/458654/31103185-130463d4-a7ac-11e7-8bcc-8bd6b8ff0b5e.png)

7) Acesse o YOURNAME.pythonanywhere.com/admin e insira posts

Use `admin` senha: `admin` para acessar. (ou altere a senha no tinydb em `cms/databases/users.json` ou no `deploy.sh`)

![step7](https://user-images.githubusercontent.com/458654/31103182-12f7c28c-a7ac-11e7-9cfe-f5aa0f5e94d6.png)

8) Veja seu post online

![step8](https://user-images.githubusercontent.com/458654/31103180-12f59584-a7ac-11e7-9847-878eb599e65b.png)



> Chegamos ao fim! agradeço se puder deixar um comentário clicando em `issues` ali em cima, pode ficar a vontade para sugerir ou criticar!

[<<-- anterior](../../../tree/cms_8_test/cms)  -  [fim mas pode continuar -->>](http://FLASK.wtf)



