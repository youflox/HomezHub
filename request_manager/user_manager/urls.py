from django.urls import path
from .views import user_login, user_signup, user_logout


urlpatterns = [
    path('', user_login, name='login' ),
    path('login', user_login, name='login'),
    path('signup', user_signup, name='signup'),
    path('logout', user_logout, name='logout'),

]
