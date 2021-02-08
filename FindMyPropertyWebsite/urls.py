from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='users')),
    path('account/', include('django.contrib.auth.urls')),
    path('', include(('findMyProperty.urls','findMyProperty'),namespace='findMyProperty')),
    path('', include(('properties.urls','properties'),namespace='properties')),

]

admin.site.site_header = 'Find my property Administration' # default: "Django Administration"
admin.site.index_title = 'Find my property Site Administration'        # default: "Site administration"
admin.site.site_title = 'Find my property admin'                  # default: "Django site admin"

