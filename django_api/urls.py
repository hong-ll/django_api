from django.conf.urls import url, include
from django.contrib import admin
from blog.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))


]
