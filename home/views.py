from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

# from .models import TestUser, TestUserInfo
#
#
# def index(request):
#     users = TestUser.objects.all()
#     context = {'users': users}
#     return render(request, 'home/index.html', context)
#
#
# def detail(request, question_id):
#     # users = TestUser.objects.get(pk=question_id)
#     # user = users.testuserinfo_set.get(pk=question_id)
#
#     # user = TestUserInfo.objects.get(pk=question_id)
#
#     users = get_object_or_404(TestUser, pk=question_id)
#     user = users.testuserinfo_set.get(pk=question_id)
#
#     return render(request, 'home/details.html', {'user': user})


from home.models import *


# def home(request):
#     all_items = ProductsTesting.objects.all()
#     product_images = ProductImagesTesting.objects.all()
#
#     d = product_images.get(id=1)
#
#     context = {
#         'products': all_items,
#         'range': range(6),
#         'product_images': product_images
#     }
#     return render(request, 'home/home.html', context)


# class IndexView(generic.ListView):
#     template_name = 'home/home.html'
#     context_object_name = 'prod'
#
#     def get_queryset(self):
#         return ProductsTesting.objects.all()


# Generic view
class HomeView(generic.ListView):
    template_name = 'home/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return ProductsTesting.objects.all()


def product(request, item_id):
    items = get_object_or_404(ProductsTesting, pk=item_id)
    return render(request, 'home/product.html')


# class ProductView(generic.DeleteView):
#     model = ProductsTesting
#     template_name = 'home/product.html'


def adding_product(request, item_id):
    items = get_object_or_404(ProductsTesting, pk=item_id)
    return render(request, 'home/adding_product.html')


def add_to_compare(request, item_id):
    items = get_object_or_404(ProductsTesting, pk=item_id)
    return render(request, 'home/addtocompare.html')


def comparison(request, item_id):
    items = get_object_or_404(ProductsTesting, pk=item_id)
    return render(request, 'home/comparison.html')


def redirect_to(request, item_id):
    items = get_object_or_404(ProductsTesting, pk=item_id)
    return render(request, 'home/redirectTo.html')


def any_product(request, item_id):
    item = get_object_or_404(ProductsTesting, pk=item_id)
    all_item = ProductsTesting.objects.all()

    get_fk = ReviewTesting.objects.filter(p_id=item_id)

    context = {
        'item': item,
        'all_item': all_item,
        'reviews': get_fk,
    }
    return render(request, 'home/anyProduct.html', context)


def add_review(request, item_id):
    item = get_object_or_404(ProductsTesting, pk=item_id)
    all_item = ProductsTesting.objects.all()

    get_fk = ReviewTesting.objects.filter(p_id=item_id)

    context = {
        'item': item,
        'all_item': all_item,
        'reviews': get_fk,
        'error_message': "Not valid product.",
    }

    if request.method == 'POST':
        q = ReviewTesting(p_id_id=item_id, email=request.POST['email_address'], comments=request.POST['review_comment'])
        q.save()

    return render(request, 'home/anyProduct.html', context)
