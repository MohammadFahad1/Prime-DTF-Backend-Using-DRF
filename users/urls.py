from django.urls import path
from users.views import CreateMessageView

urlpatterns = [
    path('send/', CreateMessageView.as_view(), name='send-message'),
]
