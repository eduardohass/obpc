from django.contrib import admin
from .models import Log, Pessoa, Endereco, Grupo, Regional


# Register your models here.
admin.site.register(Log)
admin.site.register(Pessoa)
admin.site.register(Endereco)
admin.site.register(Grupo)
admin.site.register(Regional)

