from django.urls import include, path
from .views import user, public, civic, incidence

urlpatterns = [

    path('incidence/',user.MapView.as_view(),name='incidence'),

    path('', user.home, name='home'),
    path('public/', include(([
                                 path('', public.PublicHomeView.as_view(), name='public_home'
                                                                                ''
                                                                                ''),
                             ], 'siddhesh'), namespace='public')),
    path('civic/', include(([
                                 path('', civic.CivicHomeView.as_view(), name='civic_home'),
                             ], 'siddhesh'), namespace='civic')),



]
