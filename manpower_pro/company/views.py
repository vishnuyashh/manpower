from django.shortcuts import render ,redirect
from company.models import*

# Create your views here.
def co_index(request):
    return render(request,'company/co_index.html')

