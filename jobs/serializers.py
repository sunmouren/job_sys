# encoding: utf-8
"""
@author: Sunmouren
@contact: 2826573494@qq.com
@time: 2020/3/6 10:06
@desc: 
"""
from rest_framework import serializers

from .models import WorkerInfo, RecruitInfo


class WorkerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerInfo
        fields = '__all__'


class RecruitInfoInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitInfo
        fields = '__all__'