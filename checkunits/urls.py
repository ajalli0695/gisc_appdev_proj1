__author__ = 'ajalli0695'

from django.conf.urls import patterns, include, url
from .views import WelcomeView, AboutUsView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^welcome$', WelcomeView.as_view(), name='welcome'),
    url(r'^aboutus$', AboutUsView.as_view(), name='aboutus'),

)
