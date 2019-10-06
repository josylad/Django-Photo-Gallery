from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^search/', views.search_images, name='search_results'),
    url(r'^image/(\d+)', views.get_image, name='image_results'),
    url(r'^location/(?P<location>\w{0,50})/', views.location, name='location_results'),
]
