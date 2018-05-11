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

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = {
    #         'range': range(6),
    #     }
    #     return context


def product(request, product_id):
    items = get_object_or_404(ProductsTesting, pk=product_id)
    return render(request, 'home/product.html')


# class ProductView(generic.DeleteView):
#     model = ProductsTesting
#     template_name = 'home/product.html'


def adding_product(request, product_id):
    items = get_object_or_404(ProductsTesting, pk=product_id)
    return render(request, 'home/adding_product.html')


def add_to_compare(request, product_id):
    items = get_object_or_404(ProductsTesting, pk=product_id)
    return render(request, 'home/addtocompare.html')


def comparison(request, product_id):
    items = get_object_or_404(ProductsTesting, pk=product_id)
    return render(request, 'home/comparison.html')


def redirect_to(request, product_id):
    items = get_object_or_404(ProductsTesting, pk=product_id)
    return render(request, 'home/redirectTo.html')
