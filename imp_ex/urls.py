from django.conf.urls import url, include
from django.contrib import admin
from .views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^app/', include('app.urls', namespace = 'app', app_name='app')),
    url(r'^admin/', admin.site.urls),
]
