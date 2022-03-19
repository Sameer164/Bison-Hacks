from django.urls import path
from . import views
# Our views.index currently returns the javascript logic. 
urlpatterns = [
    path("", views.home, name='home'),    
    path('search/', views.index, name = 'search'),
    path('blog/', views.blog, name = "blog"),
    path('contact/', views.contact, name='contact'),
    path('games/', views.games, name = 'games'),
    path('discussion/', views.discussion, name = 'discussion')
]
