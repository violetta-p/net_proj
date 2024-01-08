from typing import List
from django.contrib import admin
from django.db.models import QuerySet
from network.models import Element, Contact, Product


class ElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'supplier', 'debt')
    filters = ('country',)
    fields = ('id', 'name', 'level', 'supplier', 'debt')
    search_fields = ('name', 'country', )
    save_on_top = True
    actions = ['clear_dept']


    @admin.action(description='clear debt_to_the_supplier')
    def clear_dept(self, request, queryset: QuerySet) -> None:
        queryset.update(debt_to_the_supplier=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')
    search_fields = ('name', 'model', 'release_date')


admin.site.register(Element, ElementAdmin,)
admin.site.register(Product, ProductAdmin)
