
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, serializers
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, \
    UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated


from network.models import Element
from network.serializers import ElementSerializer


class ElementCreateAPIView(CreateAPIView):

    model = Element
    serializer_class = ElementSerializer
    permission_classes = [IsAuthenticated]


class ElementListAPIView(ListAPIView):

    model = Element
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country',]
    permission_classes = [IsAuthenticated]


class ElementRetrieveAPIView(RetrieveAPIView):
    serializer_class = ElementSerializer
    queryset = Element.objects.all()
    permission_classes = [IsAuthenticated,]


class ElementUpdateAPIView(UpdateAPIView):
    serializer_class = ElementSerializer
    queryset = Element.objects.all()
    permission_classes = [IsAuthenticated,]


class ElementDestroyAPIView(DestroyAPIView):
    queryset = Element.objects.all()
    permission_classes = [IsAuthenticated,]
