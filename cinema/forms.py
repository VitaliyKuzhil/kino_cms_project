from django import forms
from django.forms import modelformset_factory

from .models import Seo, Gallery, Photos


class SeoForm(forms.ModelForm):
    url_seo = forms.URLField(required=False,
                             widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Insert URL here'}))
    title_seo = forms.CharField(required=False, max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write title here'}))
    keywords_seo = forms.CharField(required=False, max_length=200,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write keywords here'}))
    description_seo = forms.CharField(required=False,
                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '6', 'placeholder': 'Write description here'}))

    class Meta:
        model = Seo
        fields = ['url_seo', 'title_seo', 'keywords_seo', 'description_seo']


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'


class PhotoForm(forms.ModelForm):
    photo = forms.ImageField(required=False,
                             label="Image",
                             widget=forms.ClearableFileInput(attrs={'class': 'form-control-file', 'id': 'file_id', 'placeholder': 'Choice main photo'}))
    class Meta:
        model = Photos
        fields = ['photo']


PhotosFormSet = modelformset_factory(
    Photos,
    form=PhotoForm,
    fields=['photo'],
    can_delete=True,
    extra=0,
    widgets={
        'photo': forms.ClearableFileInput(
            attrs={'class': 'form-control-file',
                   'placeholder': 'Choice photo'}
        )
    }
)
