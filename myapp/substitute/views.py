from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Products, Categories
from .utils.api_openFoodFacts import ApiOpenFoodFacts

# Create your views here.

def index(request):
    template = loader.get_template('substitute/index.html')
    return HttpResponse(template.render(request=request))
