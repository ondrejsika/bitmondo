from django.conf.urls import url


urlpatterns = (
    url(r'^authorize/$', 'mondo.views.authorize_view', name='authorize'),
    url(r'^logout/$', 'mondo.views.logout_view', name='logout'),
    url(r'^deactivate/$', 'mondo.views.deactivate_view', name='deactivate'),
    url(r'^address/add/$', 'mondo.views.address_add_view', name='address_add'),
    url(r'^address/remove/$', 'mondo.views.address_remove_view', name='address_remove'),
    url(r'^$', 'mondo.views.home_view', name='home'),

)

