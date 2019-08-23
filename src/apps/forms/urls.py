from django.conf.urls import url

from .views import *

app_name = 'forms'
urlpatterns = [
    url(r'^create/$', FormCreateView.as_view()),
    url(r'^all/$', FormListView.as_view()),
    url(r'^detail/(?P<pk>[0-9]+)/$', FormDetailView.as_view()),
]