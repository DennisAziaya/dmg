# yourapp/admin.py
from django.contrib import admin
from .models import Category, Subcategory, Feature


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)
    inlines = [SubcategoryInline]


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)
    inlines = [CategoryInline]


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubCategoryAdmin)
admin.site.register(Feature, FeatureAdmin)
