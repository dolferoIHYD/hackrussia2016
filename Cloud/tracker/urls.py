from django.conf.urls import url

from tracker import views

urlpatterns = [
    url(r'^$', views.monitor, name='Monitoring'),
]
