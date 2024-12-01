# criptoX

Obs.: em macOS

__1 - instalar programas básicos__

```
brew install python
brew install PostgreSQL
```
__2 - criar o virtual env__

```
python3 -m venv venv
source venv/bin/activate
```

__3 - gerenciando o postgresql__

```
brew services start postgresql
brew services list

psql postgres
postgres=# ALTER USER xxxx PASSWORD 'xxxx';
```

Obs.: o usuário do PostgreSQL no MacOS é geralmente o usuário do sistema

configure o PostgreSQL para aceitar conexão apenas autenticada

`vi /opt/homebrew/var/postgresql@14/pg_hba.conf`

modifique a linha 

`local   all             postgres                                trust`

para

`local   all             postgres                                md5`

depois, configure o PostgreSQL para aceitar conexão apenas de localhost

`vi /opt/homebrew/var/postgresql@14/postgresql.conf`

descomente a linha 

`#listen_addresses = 'localhost'`

```
brew services restart postgresql

psql -U xxxx postgres

CREATE DATABASE xxxx;
CREATE USER xxxx WITH PASSWORD 'xxxx';
GRANT ALL PRIVILEGES ON DATABASE xxxx TO xxxx;
\q
psql -U xxxx -d cryptoX
```
__4 - instalar o python3 requests__

`pip3 install requests`



...


__10 - salvar as dependências do Python__

`pip3 freeze > requirements.txt`

__11 - instalar todas dependências num novo sistema__

criar o virtual env e:

`pip3 install -r requirements.txt`



