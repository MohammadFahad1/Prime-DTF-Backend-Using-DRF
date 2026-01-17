from django.urls import path
from users.views import CreateMessageView, GoogleMapReviewViewSet
from users.views import TopHeader1ViewSet, TopHeader2ViewSet, HeroSectionButtonViewSet, GoogleMapReviewViewSet

urlpatterns = [
    path('send/', CreateMessageView.as_view(), name='send-message'),
    path('topheader1/', TopHeader1ViewSet.as_view({'get': 'list'}), name='top-header1'),
    path('topheader2/', TopHeader2ViewSet.as_view({'get': 'list'}), name='top-header2'),
    path('herobuttons/', HeroSectionButtonViewSet.as_view({'get': 'list'}), name='hero-section-buttons'),
    path('googlemapreviews/', GoogleMapReviewViewSet.as_view(), name='google-map-reviews'),
    ]
