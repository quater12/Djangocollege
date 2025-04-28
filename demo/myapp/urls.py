from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),           # /
    path('about/', views.about, name='about'),    # /about/
    path('store/', views.store, name='store'),  # /services/
    path('contact/', views.contact, name='contact'),      # /contact/
    path('blog/', views.blog, name='blog'),       # /blog/
]
