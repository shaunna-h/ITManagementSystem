from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Category, InventoryItem
from django.utils.html import strip_tags

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class InventoryItemForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), initial=0)
    class Meta:
        model = InventoryItem
        fields = ['name', 'quantity', 'category']
    def clean_name(self):
        data = self.cleaned_data['name']
        # Basic example: check for suspicious SQL injection patterns
        if ";" in data or "--" in data:
            raise forms.ValidationError("Invalid characters detected in name.")
        # Remove any HTML to avoid XSS
        data = strip_tags(data)
        return data
