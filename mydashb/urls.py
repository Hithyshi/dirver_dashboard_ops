from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    # Examples:
    url(r'^$', 'operations.views.home', name='home'),
    url(r'^operations/savetotrip/$', 'operations.views.savetotrip', name='savetotrip'),
    url(r'^operations/savetodriver/$', 'operations.views.savetodriver', name='savetodriver'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
