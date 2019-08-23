from django.conf.urls import url
from django.urls import include

app_name = 'api'
urlpatterns = [
    url(r'auth/', include('djoser.urls')),
    url(r'auth_token/', include('djoser.urls.authtoken')),
    url(r'forms/', include('apps.forms.urls')),
]