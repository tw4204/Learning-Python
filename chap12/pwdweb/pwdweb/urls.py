from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from records_app import urls as records_url
from records_app.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^records_app/', include('records_app.urls',namespace='records_app')),
    url(r'^$', HomeView.as_view(), name='home')
]
