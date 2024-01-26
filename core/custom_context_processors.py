from app.models import Category, Subcategory, Feature


def app_context(request):
    features = Feature.objects.all().filter(is_active=True)
    categories_list = Category.objects.all().filter(is_active=True)
    subcategories_list = Subcategory.objects.filter(is_active=True)
    context = {
        'features': features,
        'categories_list': categories_list,
        'subcategories_list': subcategories_list
    }
    return context

