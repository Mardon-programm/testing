from django.urls import path
from .views import ConfirmUserView

urlpatterns = [
    path('confirm/', ConfirmUserView.as_view(), name='confirm_user'),
]
