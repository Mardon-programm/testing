from modeltranslation.translator import translator, TranslationOptions
from .models import User  


class CustomUserTranslationOptions(TranslationOptions):
    fields = ('username', 'course')

translator.register(User, CustomUserTranslationOptions)
