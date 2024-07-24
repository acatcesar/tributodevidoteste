from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.views.generic import ListView, CreateView
from meuapp.forms import CreateAccountForm
from meuapp.models import Usuario
from django.shortcuts import reverse


class CreateAccount(FormView):
    template_name = "createaccount.html"
    form_class = CreateAccountForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('meuapp:list_usuariolist')

class HomehospedagemNovo(LoginRequiredMixin, CreateView):
    model = Usuario
    form_class = CreateAccountForm


class UsuarioPList(LoginRequiredMixin, ListView):
    paginate_by = 10
    model = Usuario
    template_name = 'usuariolist_list.html'

    def get_queryset(self):
        return Usuario.objects.all().order_by('id')

