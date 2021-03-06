from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render

from Orders.models import Order
from PersonalRoom.forms import FormAdditionalUser, AdditionalUser, FavoritesProducts
from PersonalRoom.models import get_or_none
from Products.models import Product


@login_required
def personal_room(request):
    orders = Order.objects.filter(username=request.user)[::-1]
    return render(request, 'personal_room.html', locals())


@login_required
def favorites(request):
    products_in_favorites = get_or_none(FavoritesProducts, user=request.user)
    return render(request, 'favorites.html', locals())


@login_required
def profile(request):
    try:
        additional_user = AdditionalUser.objects.get(user=request.user.id)
    except ObjectDoesNotExist:
        additional_user = None
    form_additional_user = FormAdditionalUser(request.POST or None, instance=additional_user)
    if request.POST:
        if form_additional_user.is_valid():
            form = form_additional_user.save(commit=False)
            if not additional_user:
                form.user = request.user
            form.save()
            if request.is_ajax():
                return HttpResponse('ok')
    return render(request, 'profile.html', locals())


def add_to_favorites(request):
    user_object, b = FavoritesProducts.objects.get_or_create(user=request.user)
    user_object.products.add(Product.objects.get(id=request.POST['id']))
    return HttpResponse('ok')


def remove_to_favorites(request):
    user_object = FavoritesProducts.objects.get(user=request.user)
    user_object.products.remove(Product.objects.get(id=request.POST['id']))
    return HttpResponse('ok')
