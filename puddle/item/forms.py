from django import forms
from .models import Item


GLOBAL_CLASS = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name', 'description','price','image',)

        widgets = {
            'category': forms.Select(attrs={
                'class': GLOBAL_CLASS
            }),
            'name': forms.TextInput(attrs={
                'class': GLOBAL_CLASS
            }),
            'description': forms.Textarea(attrs={
                'class': GLOBAL_CLASS
            }),
            'price': forms.TextInput(attrs={
                'class': GLOBAL_CLASS
            }),
            'image': forms.FileInput(attrs={
                'class': GLOBAL_CLASS
            })

        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description','price','image','is_sold')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': GLOBAL_CLASS
            }),
            'description': forms.Textarea(attrs={
                'class': GLOBAL_CLASS
            }),
            'price': forms.TextInput(attrs={
                'class': GLOBAL_CLASS
            }),
            'image': forms.FileInput(attrs={
                'class': GLOBAL_CLASS
            })

        }