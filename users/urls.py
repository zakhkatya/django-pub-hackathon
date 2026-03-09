from django.urls import path

from .views import DashboardView, LoginView, LogoutView

urlpatterns = [
    path("", LoginView.as_view()),
    path("login/", LoginView.as_view(), name="login"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
