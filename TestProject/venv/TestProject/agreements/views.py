from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Count, Avg, Sum
from django.db.models.functions import ExtractYear
from django.shortcuts import render
from rest_framework import generics
import django_filters.rest_framework

def index(request):
    return render(request, 'agreements/index.html')


def CalendarList(request):
    queryset = list(Period.objects.values('stop_date_period__year', 'stop_date_period__month').annotate(dcount=Count('stop_date_period__month')))
    month_list = [0 for i in range(12)]
    month_dict = {tmp_list: month_list for tmp_list in range(2017, 2020, 1)}

    for d in queryset:
        update_list = [0 if d['stop_date_period__month'] != i else d['dcount'] for i in range(1, 13, 1)]
        month_dict.update({d['stop_date_period__year']: update_list})
    return JsonResponse(month_dict, safe=False)
