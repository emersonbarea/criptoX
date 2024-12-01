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

vi /usr/local/var/postgres/pg_hba.conf
```

modifique a linha 

`local   all             postgres                                peer`

para

`local   all             postgres                                md5`

```
brew services restart postgresql
psql -U postgres
ALTER USER postgres PASSWORD 'sua-senha';
```





CREATE DATABASE cryptoX
```

__4 - instalar o python3 requests__

`pip3 install requests`



...


__10 - salvar as dependências do Python__

`pip3 freeze > requirements.txt`

__11 - instalar todas dependências num novo sistema__

criar o virtual env e:

`pip3 install -r requirements.txt`



