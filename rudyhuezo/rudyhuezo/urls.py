from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contact/', include('contact.urls', namespace='contact')),
    url(r'^$', include('home.urls', namespace='home')),
]
