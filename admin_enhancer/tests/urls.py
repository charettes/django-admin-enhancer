from django.contrib import admin
from django.conf.urls import patterns, include, url


admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)