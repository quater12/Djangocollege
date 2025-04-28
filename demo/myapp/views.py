from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

from .models import Toy  # Assuming your model is named 'Toy'

def store(request):
    # Fetch all items from the Toy model (or other categories if applicable)
    items = Toy.objects.all()  # Adjust the query if you want to filter specific categories
    paginator = Paginator(items, 10)  # Show 10 items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'store.html', {'page_obj': page_obj})

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')
