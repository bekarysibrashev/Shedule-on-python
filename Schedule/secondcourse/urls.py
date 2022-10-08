from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ПО 1-21', views.PO_1_21b),
    path('БНГС 1-21', views.BNGS_1_21b),
    path('ЭНГМ 1-21', views.ENGM_1_21b),
    path('ЭС 1-21', views.ES_1_21b),
    path('ЭС 2-21', views.ES_2_21b),
    path('МЕХ 1-21', views.MEX_1_21b),
    path('МЕХ 2-21', views.MEX_2_21b),
    path('ХТП 11-21', views.XTP_11_21b),
    path('ХТП 1-21', views.XTP_1_21b),
    path('АиУ 1-21', views.AIY_1_21b),
    path('ТДНГ 1-21', views.TDNG_1_21b),
]