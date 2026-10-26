from django.contrib.auth import views as auth_views, logout
from django.urls import path
from . import views

class LogoutView(auth_views.LogoutView):
    http_method_names = ['get', 'post', 'options']

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


#app_name = 'account'

urlpatterns = [
    # previous login url
    #path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
]