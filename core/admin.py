from django.contrib import admin
from models import Motorista, Associado

# Register your models here.
class MotoristaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Motorista, MotoristaAdmin)

class AssociadoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Associado, AssociadoAdmin)