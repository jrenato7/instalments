from django.shortcuts import render
from django.http import HttpResponse

from .models import InstalmentsCreditCard


def index(request):
    
    '''
    YourModel.objects.filter(datetime_published__year='2008', 
                         datetime_published__month='03', 
                         datetime_published__day='27')
    '''
    return HttpResponse('Minha primeira view')