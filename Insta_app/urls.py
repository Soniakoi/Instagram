from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url('^$',views.index,name = 'index'),
  # url(r'^search/', views.search_results, name='search_results'),
  url(r'^user/',views.user_profile,name='userProfile'),
  url(r'^profile/',views.profile,name='profile'),
  url(r'^feed/',views.feeds,name='feed'),
  url(r'^comment/',views.comments,name='comment'),
  url(r'^search/',views.search,name='search'),
  url(r'^accounts/',include('registration.backends.simple.urls')),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)