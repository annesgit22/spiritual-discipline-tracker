from django import forms
from .models import SpiritualItem


class SpiritualItemForm(forms.ModelForm):
    class Meta:
        model = SpiritualItem
        fields = ['item_type', 'name', 'description']
