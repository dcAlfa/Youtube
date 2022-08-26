from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import *
from .serializers import *


class AccountCreate(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers


class AccountRD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers


class VedioCreate(generics.CreateAPIView):
    queryset = Vedio.objects.all()
    serializer_class = VedioSerializers
    def post(self, request):
        if Account.user == self.request.user:
            ser = VedioSerializers(data=self.request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()

class VedioRD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vedio.objects.all()
    serializer_class = VedioSerializers
    def perform_destroy(self, instance):
        v = Vedio.objects.get(account=self.request.user)
        if v:
            instance.delete()
        return Response(instance)

class PleylistCreate(generics.CreateAPIView):
    queryset = Pleylist.objects.all()
    serializer_class = PleylistSerializers
    def post(self, request):
        if Account.user==self.request.user:
            ser = PleylistSerializers( data=self.request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()

class PleylistRD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pleylist.objects.all()
    serializer_class = PleylistSerializers

class ObunaCreate(generics.CreateAPIView):
    queryset = Obuna.objects.all()
    serializer_class = ObunaSerializers


class ObunaRD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Obuna.objects.all()
    serializer_class = ObunaSerializers

class LikeCreate(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializers


class LikeRD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializers


class HistoryCreate(generics.CreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializers
    def post(self, request):
        if Account.user==self.request.user:
            ser = HistorySerializers( data=self.request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()

class HistoryRD(generics.RetrieveUpdateDestroyAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializers
