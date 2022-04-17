from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('faculty_api.Api.urls')),
    path('account/', include('usersHandler.api.urls')),
    
]
