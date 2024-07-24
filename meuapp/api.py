from ninja import Router, Schema, ModelSchema
from django.http import JsonResponse
from meuapp.models import Usuario
from django.contrib import auth

router = Router()

class UsuarioLogin(Schema):
    username: str
    senha: str

class UsuarioSchema(ModelSchema):
    class Config:
        model = Usuario
        model_fields = '__all__'

@router.post('login/')
def login(request, usuario: UsuarioLogin):

    user = auth.authenticate(request, username=usuario.username, password=usuario.senha)

    if user is None:
        return JsonResponse({'error': 'E-mail ou senha inválidos'}, status=400)


    auth.login(request, user)

    return JsonResponse({'message': 'Login bem-sucedido'}, status=200)

@router.get('usuarios/')
def list_users(request):
    usuarios = Usuario.objects.all()
    usernames = [usuario.username for usuario in usuarios]
    return JsonResponse({'usuarios': usernames}, safe=False)
