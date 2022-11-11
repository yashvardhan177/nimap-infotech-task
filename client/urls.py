from django.urls import path
from client.views import ClientAPIView

urlpatterns = [
    path('clients/',ClientAPIView.as_view({'get': 'list','post':'create'})),
    path('client/<int:pk>/',ClientAPIView.as_view({'get':'get_detail', 'patch':'update'})),
]
