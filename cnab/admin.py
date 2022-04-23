from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from .models import Importation
from .views import ImportationView
from django.db import transaction


class ImportationAdmin(ModelAdmin):
    list_display = ('name', 'file')

    def save_items(self, request, obj, form, change):
        file_request = request.upload_handlers[0].file
        print(type(file_request))  # <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
        print(type(file_request.read()))  # <class 'bytes'>
        print(type(str(file_request.read())))

        #file_request = request.FILES['file']
        #file = file_request.read().decode('utf-8')


    def save_model(self, request, obj, form, change):
        with transaction.atomic():
            # This code executes inside a transaction.
            super().save_model(request, obj, form, change)
            self.save_items(request, obj, form, change)


admin.site.register(Importation, ImportationAdmin)