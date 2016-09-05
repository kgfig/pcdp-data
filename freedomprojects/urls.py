from django.conf.urls import include, url
from django.contrib import admin
from pcdpdata import urls as pcdpdata_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'freedomprojects.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^pcdpdata/', include(pcdpdata_urls, namespace='pcdpdata')),
    # url(r'^admin/', include(admin.site.urls)),
]
