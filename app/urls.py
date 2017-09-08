
from django.conf.urls import url
from app.views import pdf, certificate

app_name = 'app'
urlpatterns = [
url(r'^$', pdf, name='pdf'),
url(r'^certificate/$', certificate, name='certificate'),

]
