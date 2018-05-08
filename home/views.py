from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404


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


def home(request):
    return render(request, 'home/home.html')


def product(request, question_id):
    return render(request, 'home/product.html')


def adding_product(request, question_id):
    return render(request, 'home/adding_product.html')


def add_to_compare(request, question_id):
    return render(request, 'home/addtocompare.html')


def comparison(request, question_id):
    return render(request, 'home/comparison.html')


def redirect_to(request, question_id):
    return render(request, 'home/redirectTo.html')
