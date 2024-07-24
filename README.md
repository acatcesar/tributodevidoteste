# Projeto Django 

## Pré-requisitos

Para instalar e executar este projeto Django, você precisa seguir estas etapas:

### Configurar o ambiente virtual (venv)


python -m venv venv


### Ativar o ambiente virtual:

## No Windows:

venv\Scripts\activate

## No macOS/Linux:

source venv/bin/activate

### Instalar as dependências:


pip install -r requirements.txt

### Verificar se possui alterações das migrações do banco de dados:
python manage.py makemigrations

### Aplicar as migrações do banco de dados:
python manage.py migrate

### Executar o servidor de desenvolvimento:
python manage.py runserver

### Acessando as APIs
## Em caso de dúvidas há uma pasta no corpo deste projeto chamada ilustrações, aonde podem ser visto exemplo do funcionamento das API's 

Você pode acessar as seguintes APIs:

## Documentação Swagger/OpenAPI: http://127.0.0.1:8000/api/v2/docs#/
Utilizando a interface web de gerenciamento das APIs
Acesse a URL acima.

## Insira um usuário cadastrado no campo "authorize".

## Realize as operações de login (POST), listagem de usuários (GET) e cadastro de usuários (POST) conforme a documentação web.
### Utilizando o Postman ou outro serviço de requisições

Faça requisições para as URLs abaixo com o método Basic Auth utilizando um usuário cadastrado:
Login: POST http://127.0.0.1:8000/api/v2/usuario/login/
Listagem de usuários: GET http://127.0.0.1:8000/api/v2/usuario/usuarios/
Criação de usuário: POST http://127.0.0.1:8000/api/v2/usuario/usuarios/
