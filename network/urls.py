from django.urls import path

from network.apps import NetworkConfig
from network.views import ElementCreateAPIView, ElementListAPIView, \
    ElementRetrieveAPIView, ElementUpdateAPIView, ElementDestroyAPIView

app_name = NetworkConfig.name

urlpatterns = [
    path('element/create/', ElementCreateAPIView.as_view(), name='element_create'),
    path('element/', ElementListAPIView.as_view(), name='element_list'),
    path('element/<int:pk>/', ElementRetrieveAPIView.as_view(), name='element_get'),
    path('element/update/<int:pk>/', ElementUpdateAPIView.as_view(), name='element_update'),
    path('element/delete/<int:pk>/', ElementDestroyAPIView.as_view(), name='element_delete'),
]
