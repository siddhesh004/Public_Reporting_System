from django.urls import include,path
from .views import user, public, civic

urlpatterns = [

        path('', user.home, name='home'),

    ]