from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('<int:question_id>/result', views.results, name='results'),
    path('<int:product_id>/', views.product, name='product'),
    path('<int:product_id>/addingproduct', views.adding_product, name='adding_product'),
    path('<int:product_id>/add_to_compare', views.add_to_compare, name='add_to_compare'),
    path('<int:product_id>/comparison', views.comparison, name='comparison'),
    path('<int:product_id>/redirect_to', views.redirect_to, name='redirect_to'),
]
