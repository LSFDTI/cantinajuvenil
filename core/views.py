from django.shortcuts import render
from django.http import HttpResponse
from .models import Campista


def home(request):
	context = {'mensagem':'Mamba'}
	return render(request,'base.html',context)

def campistas(request):
	campistas = Campista.objects.all()
	return render(request, 'core/campistas.html',{'campistas':campistas} )

# Create your views here.
