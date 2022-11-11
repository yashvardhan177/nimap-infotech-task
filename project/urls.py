from django.urls import path
from project.views import ProjectAPIView

urlpatterns = [
   path('projects/',ProjectAPIView.as_view({'get':'list'})), 
   path('clients/<int:pk>/projects/',ProjectAPIView.as_view({'post':'create'})), 
]
