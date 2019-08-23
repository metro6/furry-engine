from django.conf.urls import url

from .views import *

app_name = 'client_info'
urlpatterns = [
    url(r'^$', get_client_info, name='client_info'),
]