from django.urls import path
from  .import views
from django.conf import settings
from django.conf.urls.static import static  # static is a function which give permission to use media in this url pattern
urlpatterns = [
   
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('contact/', views.contact, name='contact'),
   path('skill/', views.skill, name='skill'),


]

# give permission to use meddia with this url
if settings.DEBUG:
   urlpatterns+=static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)