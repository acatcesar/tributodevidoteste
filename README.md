Projeto Django 

Pré-requisitos
Para instalar e executar este projeto Django, você precisa seguir estas etapas:

Configurar o ambiente virtual (venv):
bash
Copiar código
python -m venv venv
Ativar o ambiente virtual:

No Windows:
bash
venv\Scripts\activate

No macOS/Linux:
bash
source venv/bin/activate
Instalar as dependências:

bash
pip install -r requirements.txt
Aplicar as migrações do banco de dados:

bash
python manage.py makemigrations
python manage.py migrate

Executar o servidor de desenvolvimento:
python manage.py runserver

Acessando as APIs
Você pode acessar as seguintes APIs:

Documentação Swagger/OpenAPI: http://127.0.0.1:8000/api/v2/docs#/
Utilizando a interface web de gerenciamento das APIs
Acesse a URL acima.

Insira um usuário cadastrado no campo "authorize".

Realize as operações de login (POST), listagem de usuários (GET) e cadastro de usuários (POST) conforme a documentação web.
Utilizando o Postman ou outro serviço de requisições
Faça requisições para as URLs abaixo com o método Basic Auth utilizando um usuário cadastrado:
Login: POST http://127.0.0.1:8000/api/v2/usuario/login/
Listagem de usuários: GET http://127.0.0.1:8000/api/v2/usuario/usuarios/
Criação de usuário: POST http://127.0.0.1:8000/api/v2/usuario/usuarios/
