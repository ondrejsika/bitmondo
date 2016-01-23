from django.conf.urls import url


urlpatterns = (
    url(r'^authorize/$', 'mondo.views.authorize_view', name='authorize'),
    url(r'^disconnect/$', 'mondo.views.disconnect_view', name='disconnect'),
    url(r'^$', 'mondo.views.home_view', name='home'),

)

