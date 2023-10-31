from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import formset_factory, modelformset_factory

from core.models import *
from cinema.models import Photos, GalleryPhotos, Movies
from core.forms import *
from cinema.forms import SeoForm, PhotosFormSet, PhotoForm

# import log
import logging

# Create logger
logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)

# Create handler for logger
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create format to display
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(console_handler)


# Create your views here.
def base_user(request):
    return render(request, 'cinema/home_page.html')


def news_view(request):
    news = NewsPage.objects.all()
    context = {'news': news}
    if request.user.is_superuser:
        return render(request, 'core/news_admin.html', context)
    else:
        return render(request, 'core/news_user.html', context)


def detail_news(request, pk):
    even = get_object_or_404(NewsPage, pk=pk)
    context = {'even': even}
    return render(request, 'core/detail_news.html', context)


@permission_required('is_superuser')
def add_news(request):
    if request.method == 'POST':
        news_form = NewsPageForm(request.POST, request.FILES)
        seo_form = SeoForm(request.POST)
        if news_form.is_valid() and seo_form.is_valid():
            news_form.save()
            seo_form.save()
            return redirect('core:news')
    else:
        news_form = NewsPageForm()
        seo_form = SeoForm()
    return render(request, 'core/create_news.html', {'news_form': news_form, 'seo_form': seo_form})


@permission_required('is_superuser')
def edit_news(request, pk):
    news = get_object_or_404(NewsPage, pk=pk)
    if request.method == 'POST':
        news_form = SharesPageForm(request.POST or None, instance=news)
        seo_form = SeoForm(request.POST or None, instance=news.seo)
        if news_form.is_valid() and seo_form.is_valid():
            news_form.save()
            seo_form.save()
            return redirect('user:news_admin')
    else:
        news_form = SharesPageForm(instance=news)
        seo_form = SeoForm(instance=news.seo)
    context = {'news_form': news_form, 'seo_form': seo_form, 'news': news}
    return render(request, 'core/edit_news.html', context)


@permission_required('is_superuser')
def delete_news(request, pk):
    del_page = get_object_or_404(NewsPage, pk=pk)
    del_page.delete()
    return redirect('user:news_admin')


def about_cinema_view(request):
    return render(request, 'core/about_cinema_page.html')


def cafe_bar_view(request):
    return render(request, 'core/cafe_bar.html')


def vip_hall_view(request):
    return render(request, 'core/vip_hall.html')


def children_room_view(request):
    return render(request, 'core/children_room.html')


def advertise_view(request):
    return render(request, 'core/advertise.html')


def shares_view(request):
    shares = SharesPage.objects.all()
    context = {'shares': shares}
    if request.user.is_superuser:
        return render(request, 'core/shares_admin.html', context)
    else:
        return render(request, 'core/shares_user.html', context)


@permission_required('is_superuser')
def add_shares(request):
    if request.method == 'POST':
        shares_form = SharesPageForm(request.POST, request.FILES)
        seo_form = SeoForm(request.POST)
        if shares_form.is_valid() and seo_form.is_valid():
            shares_form.save()
            seo_form.save()
            return redirect('user:shares_admin')
    else:
        shares_form = SharesPageForm()
        seo_form = SeoForm()
    return render(request, 'core/create_shares.html', {'shares_form': shares_form, 'seo_form': seo_form})


def detail_shares(request, pk):
    even = get_object_or_404(SharesPage, pk=pk)
    context = {'even': even}
    return render(request, 'core/detail_shares.html', context)


@permission_required('is_superuser')
def edit_shares(request, pk):
    share = get_object_or_404(SharesPage, pk=pk)
    if request.method == 'POST':
        share_form = SharesPageForm(request.POST or None, instance=share)
        seo_form = SeoForm(request.POST or None, instance=share.seo)
        if share_form.is_valid() and seo_form.is_valid():
            share_form.save()
            seo_form.save()
            return redirect('user:shares_admin')
    else:
        share_form = SharesPageForm(instance=share)
        seo_form = SeoForm(instance=share.seo)
    context = {'share_form': share_form, 'seo_form': seo_form, 'share': share}
    return render(request, 'core/edit_shares.html', context)


@permission_required('is_superuser')
def delete_shares(request, pk):
    del_page = get_object_or_404(SharesPage, pk=pk)
    del_page.delete()
    return redirect('user:shares_admin')


def mobile_app(request):
    return render(request, 'core/mobile_app.html')


def contacts_view(request):
    return render(request, 'core/contacts.html')


def custom_page_view(request):
    return render(request, 'core/custom_page.html')


@permission_required('is_superuser')
def list_pages(request):
    pages = Pages.objects.all()
    context = {'pages': pages}
    return render(request, 'core/list_pages.html', context)


@permission_required('is_superuser')
def create_page(request):
    if request.method == 'POST':
        custom_form = CustomPageForm(request.POST, request.FILES)
        seo_form = SeoForm(request.POST)
        if custom_form.is_valid() and seo_form.is_valid():
            custom_form.save()
            seo_form.save()
            return redirect('user:list_pages_admin')
    else:
        custom_form = CustomPageForm()
        seo_form = SeoForm()
    return render(request, 'core/create_page.html', {'custom_form': custom_form, 'seo_form': seo_form})


@permission_required('is_superuser')
def edit_pages(request, name_page):
    page = get_object_or_404(Pages, name_page=name_page)

    home = HomePage.objects.first()
    about_cinema = AboutCinemaPage.objects.first()
    cafe_bar = CafeBarPage.objects.first()
    vip_hall = VipHallPage.objects.first()
    advertise = AdvertisePage.objects.first()
    children_room = ChildrenRoomPage.objects.first()

    if page.name_page == home.name_page:
        if request.method == 'POST':
            home_form = HomePageForm(request.POST or None, instance=home)
            home_seo_form = SeoForm(request.POST or None, instance=home.seo_page)
            if home_form.is_valid() and home_seo_form.is_valid():
                home_form.save()
                home_seo_form.save()
        else:
            home_form = HomePageForm(instance=home)
            home_seo_form = SeoForm(instance=home.seo_page)
        context = {'home_form': home_form, 'home_seo_form': home_seo_form,
                   'page': page.name_page, 'home': home.name_page}

    elif page.name_page == about_cinema.name_page:
        if request.method == 'POST':
            about_cinema_form = AboutCinemaPageForm(request.POST or None, instance=about_cinema)
            about_cinema_seo_form = SeoForm(request.POST or None, instance=about_cinema.seo_page)

            if about_cinema_form.is_valid() and about_cinema_seo_form.is_valid():
                about_cinema_form.save()
                about_cinema_seo_form.save()
        else:
            about_cinema_form = AboutCinemaPageForm(instance=about_cinema)
            about_cinema_seo_form = SeoForm(instance=about_cinema.seo_page)
        context = {'about_cinema_form': about_cinema_form, 'about_cinema_seo_form': about_cinema_seo_form,
                   'page': page.name_page, 'about_cinema': about_cinema.name_page}

    elif page.name_page == cafe_bar.name_page:
        if request.method == 'POST':
            cafe_bar_form = CafeBarPageForm(request.POST or None, instance=cafe_bar)
            cafe_bar_seo_form = SeoForm(request.POST or None, instance=cafe_bar.seo_page)
            if cafe_bar_form.is_valid() and cafe_bar_seo_form.is_valid():
                cafe_bar_form.save()
                cafe_bar_seo_form.save()
        else:
            cafe_bar_form = CafeBarPageForm(instance=cafe_bar)
            cafe_bar_seo_form = SeoForm(instance=cafe_bar.seo_page)
        context = {'cafe_bar_form': cafe_bar_form, 'cafe_bar_seo_form': cafe_bar_seo_form,
                   'page': page.name_page, 'cafe_bar': cafe_bar.name_page}

    elif page.name_page == vip_hall.name_page:
        if request.method == 'POST':
            vip_hall_form = VipHallPageForm(request.POST or None, instance=vip_hall)
            vip_hall_seo_form = SeoForm(request.POST or None, instance=vip_hall.seo_page)
            if vip_hall_form.is_valid() and vip_hall_seo_form.is_valid():
                vip_hall_form.save()
                vip_hall_seo_form.save()
        else:
            vip_hall_form = VipHallPageForm(instance=vip_hall)
            vip_hall_seo_form = SeoForm(instance=vip_hall.seo_page)
        context = {'vip_hall_form': vip_hall_form, 'vip_hall_seo_form': vip_hall_seo_form,
                   'page': page.name_page, 'vip_hall': vip_hall.name_page}

    elif page.name_page == advertise.name_page:
        # If method POST
        if request.method == 'POST':
            logger.info("It's POST response for advertise")

            logger.info(f'POST: {request.POST}')

            logger.info(f'FILES: {request.FILES}')

            advertise_form = AdvertisePageForm(request.POST or None, instance=advertise)
            # print('advertise_form: ', advertise_form)

            formset = PhotosFormSet(request.POST or None, request.FILES or None, prefix='photo')
            logger.info(f'Formset: {formset}')

            advertise_seo_form = SeoForm(request.POST or None, instance=advertise.seo_page)
            # print('advertise_seo_form: ', advertise_seo_form)

            if advertise_form.is_valid() and advertise_seo_form.is_valid():
                logger.info('isValid')
                # Оновити основну інформацію про рекламу
                advertise_form.save(commit=False)

                # Оновити або створити основне фото (головне зображення)
                main_photo = request.FILES.get('main_photo')
                logger.info(f'MainPhoto: {main_photo}')
                if main_photo:
                    logger.info('Main Photo Change')
                    advertise_form.main_photo = main_photo

                gallery, created = Gallery.objects.get_or_create(name_gallery=f'Gallery for {page.name_page}')
                logger.info(f'gallery: {gallery}')

                # print('page: ', page.pk)
                # print('created: ', created)
                # print('gallery: ', gallery)
                if created:
                    advertise.gallery_page = gallery
                    advertise.save()

                for img_form in formset:
                    print('img_form: ', img_form)
                    if img_form.is_valid():
                        img = img_form.save(commit=False)
                        existing_photo = GalleryPhotos.objects.filter(gallery=gallery, photos__photo=img.photo).first()
                        print('existing_photo: ', existing_photo)

                        if not existing_photo:
                            img.save()
                            GalleryPhotos.objects.create(gallery=gallery, photos=img)

                advertise_form.save()
                advertise_seo_form.save()

        if request.method == 'GET':
            logger.info("It's Get response for advertise")

            advertise_form = AdvertisePageForm(instance=advertise)
            logger.info(f'Get advertise form: {advertise}')

            formset = PhotosFormSet(queryset=Photos.objects.filter(gallery=advertise.gallery_page), prefix='photo')
            logger.info(f'Get formset: {formset}')

            advertise_seo_form = SeoForm(instance=advertise.seo_page)
            logger.info(f'Get seo form: {advertise_seo_form}')

        context = {'advertise_form': advertise_form, 'formset': formset, 'advertise_seo_form': advertise_seo_form,
                   'page': page.name_page, 'advertise': advertise.name_page}

    elif page.name_page == children_room.name_page:
        if request.method == 'POST':
            children_room_form = ChildrenRoomPageForm(request.POST, instance=children_room)
            formset = PhotosFormSet(request.POST, request.FILES, queryset=Photos.objects.none())
            children_room_seo_form = SeoForm(request.POST, instance=children_room.seo_page)
            if children_room_form.is_valid() and formset.is_valid() and children_room_seo_form.is_valid():
                children_room_form.save()
                children_room_seo_form.save()

                for form in formset:
                    if form.cleaned_data.get('photo'):
                        img_obj = form.save(commit=False)
                        img_obj.gallery = children_room.gallery_page
                        img_obj.save()
            return redirect('user:list_pages_admin')
        else:
            children_room_form = ChildrenRoomPageForm(instance=children_room)
            formset = PhotosFormSet(queryset=Photos.objects.filter(gallery=page.gallery_page))

            children_room_seo_form = SeoForm(instance=children_room.seo_page)
        context = {'children_room_form': children_room_form, 'formset': formset,
                   'children_room_seo_form': children_room_seo_form,
                   'page': page.name_page, 'children_room': page.name_page}

    elif page.name_page == 'Contacts page':
        ContactPageFormSet = formset_factory(ContactsPageForm, extra=0)
        contacts = ContactPage.objects.all()

        if request.method == 'POST':
            contacts_formset = ContactPageFormSet(request.POST or None, prefix='contacts')
            contacts_seo_form = SeoForm(request.POST or None)

            if contacts_formset.is_valid() and contacts_seo_form.is_valid():
                for form in contacts_formset:
                    form.save()
                contacts_seo_form.save()

        else:
            initial_data = [{'name_cinema': contact.name_cinema,
                             'logo_cinema': contact.logo_cinema,
                             'address_cinema': contact.address_cinema,
                             'location_cinema': contact.location_cinema} for contact in contacts]
            contacts_formset = ContactPageFormSet(prefix='contacts', initial=initial_data)
            contacts_seo_form = SeoForm(instance=page.seo_page)

        context = {
            'contacts_formset': contacts_formset,
            'contacts_seo_form': contacts_seo_form,
            'page': page.name_page,
            'contacts': 'Contacts page'
        }

    else:
        custom = CustomPage.objects.get(name_page=name_page)
        if request.method == 'POST':
            custom_form = CustomPageForm(request.POST or None, instance=custom)
            formset = PhotosFormSet(request.POST, request.FILES, queryset=Photos.objects.none())
            custom_seo_form = SeoForm(request.POST or None, instance=custom.seo_page)
            if custom_form.is_valid() and custom_seo_form.is_valid():
                custom_form.save()
                custom_seo_form.save()

                for form in formset:
                    if form.cleaned_data.get('photo'):
                        img_obj = form.save(commit=False)
                        img_obj.gallery = children_room.gallery_page
                        img_obj.save()
            return redirect('user:list_pages_admin')
        if request.method == 'GET':
            custom_form = CustomPageForm(instance=custom)
            formset = PhotosFormSet(queryset=Photos.objects.filter(gallery=page.gallery_page))
            custom_seo_form = SeoForm(instance=custom.seo_page)
        context = {'custom_form': custom_form, 'custom_seo_form': custom_seo_form, 'formset': formset,
                   'page': page.name_page, 'custom': custom.name_page}

    return render(request, 'cinema/edit_pages.html', context)


@permission_required('is_superuser')
def delete_page(request, id_page):
    del_page = Pages.objects.get(pk=id_page)
    del_page.delete()
    return redirect('user:list_pages_admin')


@permission_required('is_superuser')
def add_contact(request, name_page):
    if request.method == 'POST':
        contact_form = ContactsPageForm(request.POST, request.FILES)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('user:edit_pages', name_page=name_page)
    else:
        contact_form = ContactsPageForm()
    return render(request, 'core/add_contact.html', {'contact_form': contact_form, 'name_page': name_page})


@permission_required('is_superuser')
def mailing_view(request):
    return render(request, 'core/mailing.html')
