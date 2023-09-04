from django import forms
from .models import Seo, Gallery, Photos


class SeoForm(forms.ModelForm):
    url_seo = forms.URLField(required=False,
                             widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Insert URL here'}))
    title_seo = forms.CharField(required=False, max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write title here'}))
    keywords_seo = forms.CharField(required=False, max_length=200,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write keywords here'}))
    description_seo = forms.CharField(required=False,
                                      widget=forms.Textarea(attrs={'class': 'form-control', 'row': '3', 'placeholder': 'Write description here'}))

    class Meta:
        model = Seo
        fields = ['url_seo', 'title_seo', 'keywords_seo', 'description_seo']


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = '__all__'
