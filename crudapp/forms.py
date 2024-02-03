from django import forms
from . models import Publisher, Book

class PublisherForm(forms.ModelForm):
    class Meta:
        model=Publisher
        fields=['name']

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter publisher name'}),


        }
    


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your book name'}),
            'author':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter author name'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your book price'}),
            
            'publisher':forms.Select(attrs={'class':'form-control','placeholder':'Select publisher name'})

        }