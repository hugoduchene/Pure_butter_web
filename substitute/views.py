from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Products, UserRecord
from .utils.api_openFoodFacts import ApiOpenFoodFacts
from django.views.generic.edit import FormView
from .forms import SearchSubstitute, SearchMeat

# Create your views here.
form_header = SearchMeat()

def mention(request):
    template = loader.get_template('substitute/mentions.html')
    return HttpResponse(template.render(request=request))

def index(request):
    form = SearchSubstitute()
    context = {
        'form': form,
        'form_header': form_header
    }

    template = loader.get_template('substitute/index.html')
    return HttpResponse(template.render(request=request, context=context))

def result(request):
    if request.method == 'POST':
         form = SearchSubstitute(request.POST)
         if form.is_valid():
             name_product = form.cleaned_data['input_product_name']
             query_product = Products.objects.filter(product_name__icontains= name_product)
             if len(query_product) > 0:
                 category_product = query_product[0].id_category
                 best_products = Products.objects.filter(id_category=category_product).order_by('score_grade')[:6]
                 context = {
                    'form_header': form_header,
                    "search_food": query_product[0],
                    "prod" : best_products
                    }
                 template = loader.get_template('substitute/result.html')
                 return HttpResponse(template.render(request=request, context= context))
             else:
                 return redirect('index')
         else:
             pass
    else:
        template = loader.get_template('substitute/404.html')
        return HttpResponse(template.render(request=request))

def search_meat(request, name_product):
    if request.method == 'GET':
        query_product = Products.objects.filter(product_name__iexact = name_product)
        context = {
            'form_header': form_header,
            'prod' : query_product[0]
         }
        template = loader.get_template('substitute/food.html')
        return HttpResponse(template.render(request=request, context=context))

def save_food(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id_product = request.POST['id_product']
            obj_prod = Products.objects.get(id=id_product)
            req_prod = UserRecord(id_user=request.user, id_product=obj_prod)
            req_prod.save()
            return redirect('myfood')
        else:
            template = loader.get_template('substitute/404.html')
            return HttpResponse(template.render(request=request))
    else:
        return redirect('registration')


def get_product_record(request):
    if request.user.is_authenticated:
        list_product = [prod.id_product for prod in UserRecord.objects.filter(id_user=request.user.id)]

        context= {
            'form_header': form_header,
            'products' : list_product
        }
        template = loader.get_template('substitute/myfood.html')
        return HttpResponse(template.render(request=request, context=context))
    else:
        return redirect('registration')
