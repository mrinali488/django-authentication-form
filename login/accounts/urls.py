from django.urls import path
from . import views
from .views import signup_view
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', views.index_view, name="home"),
    path('profile/', views.profile_view, name="profile_url"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('signup/', signup_view.as_view(), name='signup_url'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]