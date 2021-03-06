from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', hello.views.profile, name='perfil'),
    path('accounts/profile/solicitudes/', hello.views.solicitudes, name='solicitudes'),
    path('accounts/profile/solicitudes/helper/', hello.views.helper, name='helper'),
    path('accounts/profile/solicitudes/helper/succes', hello.views.Succes, name='Succes'),
    path('accounts/profile/pos/', hello.views.po, name='pos'),
]
