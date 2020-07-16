from django import forms

class SearchSubstitute(forms.Form):
    input_product_name = forms.CharField(
        max_length=100,
        widget = forms.TextInput(attrs={
            'class' : 'form-control search_button',
            'placeholder': 'Produits',
            'id' : 'SearchSubstitute'
        }))

class SearchMeat(forms.Form):
    input_product_name = forms.CharField(
        max_length=100,
        widget = forms.TextInput(attrs={
            'class' : 'form-control mr-sm-2',
            'placeholder': 'Search'
        })
    )
