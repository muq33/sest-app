
# SESt-App

Um aplicativo desenvolvido inteiramente em python, que busca dar vida a um aplicativo mobile para Semana da Estatística (SESt)


## Instalação
Requerimentos Python:

Caso 1:

Execute o arquivo installer.py

Caso 2:

Abra o console do python na pasta clonada e digite

```bash
  pip install -r ./requirements.txt
```
Autenticação:

Caso 1:

Depois realize a instalação do SGBD [PostgreSQL](https://www.postgresql.org/) 
e durante a instalação digite a seguinte combinação para usuario/senha:

```bash
  usuario : postgres
  senha : admin 
```
Caso 2:

Deixe as linhas 65-74(função de login) do arquivo main.py dessa forma:

```bash
        if self.login_screen.ids.user.text=='1' and self.login_screen.ids.password.text=='1':
            return self.switch_screen('menu')
#         query = self.sql.select_db('app','auth', {'usuario': self.login_screen.ids.user.text,
#                                                 'senha' : hashlib.sha256(self.login_screen.ids.password.text.encode()).hexdigest()})
#         if query:
#             self.user_cpf = query['cpf']
#             return self.switch_screen('menu')
#         else:
#             return self.dialog_box('Falha', 'Não foi encontrado uma conta com essas informações')
```
Obs: Dessa forma, seu usuário de autenticação dentro do aplicativo sempre será da seguinte forma:

```bash
  usuario : 1
  senha : 1
```
Obs2: Dessa forma você não precisa de um SGBD instalado e portanto não poderá realizar um registro de conta.
## Roadmap

- Otimizar o desempenho do código de forma geral.

- Terminar de implementar a biblioteca de autenticação de registro do usuário, a fim de garantir mais segurança.

-



## Autores

- [@muq33](https://github.com/muq33)


## Licença

[MIT](https://choosealicense.com/licenses/mit/)

