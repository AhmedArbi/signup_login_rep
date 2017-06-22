from django.conf.urls import url
from . import views

app_name = 'sigin_login_app'
urlpatterns = [
    url(r'^$', views.login ),
    url(r'^signup$', views.signup),
    url(r'^_signup$', views.signup_, name='_signup')
]