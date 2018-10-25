from django.contrib import admin

# Register your models here.
from app.models import Color, Animal, Respondent


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass

@admin.register(Respondent)
class RespondentAdmin(admin.ModelAdmin):
    pass