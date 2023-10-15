from django import forms
from phonenumber_field.formfields import PhoneNumberField
from core.models import HomePage, AboutCinemaPage, CafeBarPage, VipHallPage, AdvertisePage, ChildrenRoomPage, \
    ContactPage, CustomPage, NewsPage, SharesPage
from core.constants import STATUS_CHOICES


class HomePageForm(forms.ModelForm):
    phone1 = PhoneNumberField(required=False, label='Phone Number',
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': 'Write phone here'}))
    phone2 = PhoneNumberField(required=False, label='Phone Number',
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': 'Write phone here'}))
    seo_text = forms.CharField(required=False, label='SEO text',
                               widget=forms.Textarea(
                                   attrs={'class': 'form-control', "rows": '3', 'placeholder': 'Write seo text here'}))
    status_page = forms.BooleanField(required=False, label="Status page", initial=True,
                                     widget=forms.RadioSelect(choices=STATUS_CHOICES,
                                                              attrs={'class': 'form-check-inline'}))

    class Meta:
        model = HomePage
        fields = ['phone1', 'phone2', 'seo_text', 'status_page']


class AboutCinemaPageForm(forms.ModelForm):
    name_page = forms.CharField(required=True, max_length=50, label="Page Name",
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Write name page here'}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'row': '3',
                                                               'placeholder': 'Write description here'}))
    main_photo = forms.ImageField(required=False, label="Image",
                                  widget=forms.ClearableFileInput(attrs={'class': 'form-control-file',
                                                                         'id': 'file_id',
                                                                         'placeholder': 'Choice main photo'}))
    status_page = forms.BooleanField(label="Status page", initial=True,
                                     widget=forms.RadioSelect(choices=STATUS_CHOICES,
                                                              attrs={'class': 'form-check-inline'}))

    class Meta:
        model = AboutCinemaPage
        fields = ['name_page', 'description', 'main_photo', 'status_page']


class CafeBarPageForm(forms.ModelForm):
    name_page = forms.CharField(required=True, max_length=50, label="Page Name",
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Write name page here'}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'row': '3',
                                                               'placeholder': 'Write description here'}))
    main_photo = forms.ImageField(required=False, label="main_photo",
                                  widget=forms.ClearableFileInput(attrs={'class': 'form-control-file',
                                                                         'id': 'file_id',
                                                                         'placeholder': 'Choice main photo'}))
    menu_cafe_bar = forms.ImageField(required=False, label="menu_cafe_bar",
                                     widget=forms.ClearableFileInput(attrs={'class': 'form-control-file',
                                                                            'id': 'file_id',
                                                                            'placeholder': 'Choice main photo'}))
    status_page = forms.BooleanField(required=False, label="Status page", initial=True,
                                     widget=forms.RadioSelect(choices=STATUS_CHOICES,
                                                              attrs={'class': 'form-check-inline'}))

    class Meta:
        model = CafeBarPage
        fields = ['name_page', 'description', 'main_photo', 'menu_cafe_bar', 'status_page']


class VipHallPageForm(forms.ModelForm):
    name_page = forms.CharField(required=True, max_length=50, label="Page Name",
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Write name page here'}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'row': '3',
                                                               'placeholder': 'Write description here'}))
    main_photo = forms.ImageField(label="Image",
                                  widget=forms.ClearableFileInput(attrs={'class': 'form-control-file',
                                                                         'id': 'file_id',
                                                                         'placeholder': 'Choice main photo'}))
    status_page = forms.BooleanField(label="Status page", initial=True,
                                     widget=forms.RadioSelect(choices=STATUS_CHOICES,
                                                              attrs={'class': 'form-check-inline'}))

    class Meta:
        model = VipHallPage
        fields = ['name_page', 'description', 'main_photo', 'status_page']


class AdvertisePageForm(forms.ModelForm):
    name_page = forms.CharField(required=True, max_length=50, label="Page Name",
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Write name page here'}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '6',
                                                               'placeholder': 'Write description here'}))
    main_photo = forms.ImageField(label="Image", required=False,
                                  widget=forms.ClearableFileInput(attrs={'class': 'form-control-file',
                                                                         'id': 'file_id',
                                                                         'placeholder': 'Choice main photo'}))
    status_page = forms.BooleanField(label="Status page", initial=True,
                                     widget=forms.RadioSelect(choices=STATUS_CHOICES,
                                                              attrs={'class': 'form-check-inline'}))

    class Meta:
        model = AdvertisePage
        fields = ['name_page', 'description', 'main_photo', 'status_page']


class ChildrenRoomPageForm(forms.ModelForm):
    name_page = forms.CharField(required=True, max_length=50, label="Page Name",
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Write name page here'}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'row': '3',
                                                               'placeholder': 'Write description here'}))
    main_photo = forms.ImageField(required=False, label="Image",
                                  widget=forms.ClearableFileInput(attrs={'class': 'form-control-file',
                                                                         'id': 'file_id',
                                                                         'placeholder': 'Choice main photo'}))
    status_page = forms.BooleanField(required=False, label="Status page", initial=True,
                                     widget=forms.RadioSelect(choices=STATUS_CHOICES,
                                                              attrs={'class': 'form-check-inline'}))

    class Meta:
        model = ChildrenRoomPage
        fields = ['name_page', 'description', 'main_photo', 'status_page']


class ContactsPageForm(forms.ModelForm):
    name_cinema = forms.CharField(required=True, max_length=50, label="Cinema Name",
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Write name cinema here'}))
    logo_cinema = forms.ImageField(required=False, label="Image",
                                   widget=forms.ClearableFileInput(attrs={'class': 'form-control-file',
                                                                          'id': 'file_id',
                                                                          'placeholder': 'Choice main photo'}))
    address_cinema = forms.CharField(required=True, label='Address cinema',
                                     widget=forms.TextInput(attrs={'class': 'form-control',
                                                                   'placeholder': 'Write address for cinema here'}))
    location_cinema = forms.DecimalField(required=True, label='Location',
                                         widget=forms.TextInput(attrs={'class': 'form-control',
                                                                       'placeholder': 'Write location for cinema here'}))

    class Meta:
        model = ContactPage
        fields = ['name_cinema', 'logo_cinema', 'address_cinema', 'location_cinema']


class CustomPageForm(forms.ModelForm):
    name_page = forms.CharField(required=False, max_length=50, label="Page Name",
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Write name page here'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                               'rows': '3',
                                                                               'placeholder': 'Write description for page here'}))
    main_photo = forms.ImageField(required=False, label="Image",
                                  widget=forms.ClearableFileInput(attrs={'class': 'form-control-file',
                                                                         'id': 'file_id',
                                                                         'placeholder': 'Choice main photo'}))
    status_page = forms.BooleanField(required=False, label="Status page", initial=True,
                                     widget=forms.RadioSelect(choices=STATUS_CHOICES,
                                                              attrs={'class': 'form-check-inline'}))

    class Meta:
        model = CustomPage
        fields = ['name_page', 'description', 'main_photo', 'status_page']


class NewsPageForm(forms.ModelForm):
    name = forms.CharField(required=False, max_length=50, label="Title event",
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Write title event here'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                               'rows': '3',
                                                                               'placeholder': 'Write description for event here'}))
    main_photo = forms.ImageField(required=False, label="Image",
                                  widget=forms.ClearableFileInput(attrs={'class': 'form-control-file',
                                                                         'id': 'file_id',
                                                                         'placeholder': 'Choice main photo'}))
    url_address = forms.URLField(required=False, label="URL", help_text='Input url address to news',
                                 widget=forms.URLInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Write url address for event here'}))

    class Meta:
        model = NewsPage
        fields = ['name', 'description', 'main_photo', 'url_address']


class SharesPageForm(forms.ModelForm):
    name = forms.CharField(required=False, max_length=50, label="Title share",
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Write title share here'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                               'rows': '3',
                                                                               'placeholder': 'Write description for share here'}))
    main_photo = forms.ImageField(required=False, label="Image",
                                  widget=forms.ClearableFileInput(attrs={'class': 'form-control-file',
                                                                         'id': 'file_id',
                                                                         'placeholder': 'Choice main photo'}))
    url_address = forms.URLField(required=False, label="URL", help_text='Input url address to share',
                                 widget=forms.URLInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Write url address for share here'}))

    class Meta:
        model = SharesPage
        fields = ['name', 'description', 'main_photo', 'url_address']
