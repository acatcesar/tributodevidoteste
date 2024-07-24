from django.urls import path
from django.contrib.auth import views as auth_view


from meuapp.views import CreateAccount, UsuarioPList

app_name ='meuapp'

urlpatterns = [
    path('', UsuarioPList.as_view(), name='list_usuariolist'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('createaccount/', CreateAccount.as_view(), name='createaccount'),
]