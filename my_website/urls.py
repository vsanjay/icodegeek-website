
from django.conf.urls import url
from django.contrib import admin
from homepageapp import homepageviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepageviews.homepage),
]
