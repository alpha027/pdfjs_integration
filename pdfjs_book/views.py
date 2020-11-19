from django.shortcuts import render
from .models import Document
from django.views.decorators.clickjacking import xframe_options_exempt
# Create your views here.
@xframe_options_exempt
def first(request):
	
	docs = Document.objects.all()
	return render(request, 'home.html', {'documents':docs})

def second_pdfjs(request):
    
    docs = Document.objects.all()
    return render(request, 'pdfjs.html', {'documents':docs})

def pdf_view(request):
    
    return render(request, 'viewer.html')