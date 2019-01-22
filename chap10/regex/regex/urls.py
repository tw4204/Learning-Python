from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from entries.views import HomeView, EntryListView, EntryFormView
urlpatterns = [
    url(r'^entries/$', EntryListView.as_view(), name='entries'),
    url(r'^entries/insert$', EntryFormView.as_view(), name='insert'),
    url(r'^login/$', auth_views.LoginView, kwargs={'template_name': 'admin/login.html'},name='login'),
    url(r'^logout/$', auth_views.LogoutView,kwargs={'next_page': reverse_lazy('home')},name='logout'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls)]


