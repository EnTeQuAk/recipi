from django.contrib import admin
from django.conf.urls import url, include

from recipi.core import views as core_views


urlpatterns = [
    url(r'^$',
        core_views.IndexView.as_view(),
        name='recipi-index'),
    url(r'^editor/$',
        core_views.EditorView.as_view(),
        name='recipi-editor'),

    url(r'^account/', include('allauth.urls')),

    # Hookup our REST Api
    url(r'^api/', include('recipi.api.urls', namespace='recipi-api')),
    url(r'^api/docs/', include('rest_framework.urls', namespace='rest_framework')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
]
