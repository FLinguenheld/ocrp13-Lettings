from django.contrib import admin
from django.urls import path, include

from . import views


def test_sentry(request):
    raise ValueError(f"Error generated to test Sentry {request.user}")


urlpatterns = [
    path('', views.index, name='index'),
    path('', include('lettings.urls')),
    path('', include('profiles.urls')),
    path('admin/', admin.site.urls),

    path('sentry-debug/', test_sentry),
]
