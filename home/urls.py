from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('team/', views.team, name='team'),
    # path('<int:question_id>/result', views.results, name='results'),
    path('<int:item_id>/', views.product, name='product'),
    path('<int:item_id>/add_to_compare', views.add_to_compare, name='add_to_compare'),
    path('<int:item_id>/redirect_to', views.redirect_to, name='redirect_to'),
    path('<int:item_id>/any_product', views.any_product, name='any_product'),
    path('<int:item_id>/addreview', views.add_review, name='add_review'),
    path('<int:previtem_id>/<int:item_id>/comparison', views.comparison, name='comparison'),
    path('<int:previtem_id>/<int:item_id>/addingproduct', views.adding_product, name='adding_product'),
]
