from django.conf.urls import url


urlpatterns = (
    url(r'^authorize/$', 'mondo.views.authorize_view', name='authorize'),
    url(r'^logout/$', 'mondo.views.logout_view', name='logout'),
    url(r'^deactivate/$', 'mondo.views.deactivate_view', name='deactivate'),
    url(r'^$', 'mondo.views.home_view', name='home'),

)

