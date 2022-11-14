from django.views.generic import TemplateView, CreateView
from accounts.forms import RegisterForm
from django.urls import reverse_lazy



class RegisterView(CreateView):
    template_name = "accounts/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("accounts:register")