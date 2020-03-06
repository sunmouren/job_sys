from django.shortcuts import render

from rest_framework import viewsets

from .serializers import WorkerInfoSerializer, RecruitInfoInfoSerializer
from .models import WorkerInfo, RecruitInfo


class WorkInfoViewSet(viewsets.ModelViewSet):
    queryset = WorkerInfo.objects.all()
    serializer_class = WorkerInfoSerializer


class RecruitInfoViewSet(viewsets.ModelViewSet):
    queryset = RecruitInfo.objects.all()
    serializer_class = RecruitInfoInfoSerializer
