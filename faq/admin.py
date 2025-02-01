from django.contrib import admin
from .models import FAQ
from ckeditor.widgets import CKEditorWidget
from django import forms

class FAQForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorWidget())  # Use CKEditor for the answer field

    class Meta:
        model = FAQ
        fields = '__all__'

class FAQAdmin(admin.ModelAdmin):
    form = FAQForm

admin.site.register(FAQ, FAQAdmin)


