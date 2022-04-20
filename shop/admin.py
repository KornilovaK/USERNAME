from django.contrib import admin
from .models import Table, Reserve, Category, Menu

admin.site.register(Table)
admin.site.register(Reserve)
admin.site.register(Category)
admin.site.register(Menu)