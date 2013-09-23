from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eatwell.views.home', name='home'),
    # url(r'^eatwell/', include('eatwell.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Top down first match is applied
    url(r'^$', 'restaurants.views.home', name='home'),
    url(r'^contact/$', 'restaurants.views.contact', name='contact'),
    url(r'^restaurants/$', 'restaurants.views.restaurant_list', name='restaurant_list'),
    url(r'^restaurants/(?P<pk>\d+)/$', 'restaurants.views.restaurant_details', name='restaurant_details'),
    url(r'^restaurants/(?P<pk>\d+)/write-review$', 'restaurants.views.write_review', name='write_review')
)
