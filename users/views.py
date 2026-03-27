from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView
from ecp_auth.mixins import ECPGenerateMixin, ECPLoginMixin

from .forms import RegisterForm


class LoginView(DjangoLoginView):
    template_name = "auth/login.html"
    redirect_authenticated_user = True


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"
    login_url = "login"


class RegisterView(ECPGenerateMixin, CreateView):
    form_class = RegisterForm
    template_name = "auth/register.html"
    success_url = reverse_lazy("login")

    # Override form_valid to generate ECP certificate after user creation
    def form_valid(self, form):
        user = super().form_valid(form)
        taxpayer_id = form.cleaned_data.get("taxpayer_id")
        self.generate_ecp(user, taxpayer_id)
        return user

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard")
        return super().dispatch(request, *args, **kwargs)


class LogoutView(ECPLoginMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        logout(request)
        return redirect("login")
    
