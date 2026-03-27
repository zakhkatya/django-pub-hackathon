from django.urls import path
from .views import DashboardView, LoginView, LogoutView, RegisterView
from ecp_auth.views import ChallengeView, KeyDisplayView

urlpatterns = [
    path("", LoginView.as_view()),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("ecp/challenge/", ChallengeView.as_view(), name="ecp_challenge"),
    path("ecp/certificate/download/", KeyDisplayView.as_view(), name="ecp_certificate_download"),
]