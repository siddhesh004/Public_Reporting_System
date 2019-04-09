from django.contrib import admin
from siddhesh.models import User,Public,Civic, Incidence
from leaflet.admin import LeafletGeoAdmin
admin.site.register(Public)
admin.site.register(User)
admin.site.register(Civic)
admin.site.register(Incidence, LeafletGeoAdmin)
