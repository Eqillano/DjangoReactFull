from django.urls import path
from .views import ListingView,SearchView,RetrieveAPIView


urlpatterns = [
     path('',ListingView.as_view()),
     path('search',SearchView.as_view()),
     path('<slug>',RetrieveAPIView.as_view())
]
