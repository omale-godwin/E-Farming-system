
from django.urls import path
from . import views

urlpatterns = [
    path('searches', views.searches, name="searches" ),
    path('listings/', views.listings, name="listings"),
   path('<int:listing_id>', views.listing, name='listing'),
    path('upload/', views.upload, name="upload"),
]
