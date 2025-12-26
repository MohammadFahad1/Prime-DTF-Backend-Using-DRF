from django.urls import path
from product.views import ReadyToPress

# Create your views here.

urlpatterns = [
    path('list/', ReadyToPress.as_view(), name='ready-to-press-list'),
]
