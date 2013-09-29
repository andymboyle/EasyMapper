from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'easymapper.views.locations', name='locations'),
    url(r'^$', 'easymapper.views.json_full_feed', name='json_full_feed'),
)
