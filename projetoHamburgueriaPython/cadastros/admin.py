from django.contrib import admin

# Register your models here.

from .models import Produto, Carrinho

admin.site.register(Produto)
admin.site.register(Carrinho)
#


