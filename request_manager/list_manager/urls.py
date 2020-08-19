from django.urls import path, include
from .views import home, newRequests, requestById


urlpatterns = [
    path('', home, name='home'),
    path('requests', newRequests, name='requests'),
    path('request/<int:id>', requestById, name='reqid' )

]