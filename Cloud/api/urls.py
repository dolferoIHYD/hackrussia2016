from django.conf.urls import url
from api import views as api_views

urlpatterns = [
    url(r'^', api_views.receive, name='receive'),
]
