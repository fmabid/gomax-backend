from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    # path('<int:question_id>/result', views.results, name='results'),
    path('<int:question_id>/', views.product, name='product'),
    path('<int:question_id>/addingproduct', views.adding_product, name='adding_product'),
    path('<int:question_id>/add_to_compare', views.add_to_compare, name='add_to_compare'),
    path('<int:question_id>/comparison', views.comparison, name='comparison'),
    path('<int:question_id>/redirect_to', views.redirect_to, name='redirect_to'),
]
