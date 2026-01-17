from django.urls import path
from product.views import ReadyToPress, CustomDesignViewSet, ProductViewSet

# Create your views here.

urlpatterns = [
    path('list/', ReadyToPress.as_view(), name='ready-to-press-list'),
    path('customdesign/', CustomDesignViewSet.as_view(), name='custom-design-list'),
    path('products/', ProductViewSet.as_view(), name='product-list'),
]
