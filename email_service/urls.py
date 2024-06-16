from django.urls import path
from email_service.api.views import EmailAPIView

urlpatterns=[ 
    path('send/',EmailAPIView.as_view(),name='email')
]