from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . forms import LoginForm

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.pages_data, name='pages_data'),
    path('pages/', views.pages, name='pages'),
    path('compare/<int:id>/', views.compare, name='compare'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.logout_view, name='logout')
]