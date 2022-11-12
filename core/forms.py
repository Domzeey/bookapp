from django import forms
from .models import book


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = ["title", "content", "author", "cover_image"]

