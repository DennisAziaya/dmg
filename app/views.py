from django.shortcuts import render, get_object_or_404

# Create your views here.
# yourapp/views.py
from django.shortcuts import render
from .models import Category, Subcategory, Feature


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'accounts/dashboard.html', {'detail': category, 'cat': 'cat'})


def feature_detail(request, pk):
    feature = get_object_or_404(Feature, pk=pk)
    return render(request, 'accounts/dashboard.html', {'feature': feature, 'ft': 'ft'})


def sub_category_detail(request, pk):
    sub_category = get_object_or_404(Subcategory, pk=pk)
    return render(request, 'app/category/sub-category.html', {'detail': sub_category})


def sub_category_search(request):
    query = request.GET.get('search', '')
    sub_categories_list = Subcategory.objects.filter(name__icontains=query)
    context = {'data_lists': sub_categories_list, 'search': 'search', 'search_term': query}
    return render(request, 'accounts/dashboard.html', context)
