from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueForDateValidator


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        # fields = '__all__'
        fields = ['id', 'stop_date_period']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class NegotiatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negotiator
        fields = '__all__'


class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = '__all__'


class BridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bridge
        fields = '__all__'

   

class  AgreementFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = ['id']