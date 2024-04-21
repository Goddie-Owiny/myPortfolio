from django.urls import path
from portfo import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('blog/', views.blog, name='blog'),
]