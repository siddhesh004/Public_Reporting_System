from django.urls import include, path
from .views import user, public, civic

urlpatterns = [
    path('', user.home, name='home'),
    path('public/', include(([
                                 path('', public.PublicHomeView.as_view(), name='public_home'
                                                                                ''
                                                                                ''),
                             ], 'user'), namespace='public')),
    path('civic/', include(([
                                 path('', civic.CivicHomeView.as_view(), name='civic_home'),
                             ], 'user'), namespace='civic')),



]
