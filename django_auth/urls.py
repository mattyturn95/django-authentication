from django.conf.urls import url
from django.contrib import admin
from accounts.views import index, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^accounts/logout/$', logout, name='logout')

]
