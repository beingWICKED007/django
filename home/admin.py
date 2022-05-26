from django.contrib import admin
from .models import *


# Register your models here.

class CategeoryAdmin(admin.ModelAdmin):
    list_display =  ('id','name','slug')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategeoryAdmin)


admin.site.register(Price)
admin.site.register(Color)
admin.site.register(Size)


class ProductAdmin(admin.ModelAdmin):
    list_display =  ('id','name','slug','color',)
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product,ProductAdmin)


admin.site.register(Contact)
admin.site.register(Otp)
admin.site.register(HomeCategories)
# admin.site.register(HomeSubCategories)
admin.site.register(HomeProduct)





