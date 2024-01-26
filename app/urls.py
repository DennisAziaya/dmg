from django.urls import path

from app.views import sub_category_detail, category_detail, sub_category_search, feature_detail

app_name = 'app'

urlpatterns = [
    path('feature/<int:pk>/', feature_detail, name='feature'),
    path('feature/categories/<int:pk>/', category_detail, name='category'),
    path('feature/categories/sub-category/<int:pk>/', sub_category_detail, name='sub_category'),
    path('feature/categories/sub-categories/search/', sub_category_search, name='sub_category_search')

]
