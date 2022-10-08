from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('АиУ 1-22', views.AIY_1_22),
    path('ПО 1-22', views.PO_1_22),
    path('БНГС 1-22', views.BNGS_1_22),
    path('ЭНГМ 1-22', views.ENGM_1_22),
    path('ЭНГМ 2-22', views.ENGM_2_22),
    path('ЭС 1-22', views.ES_1_22),
    path('ЭС 2-22', views.ES_2_22),
    path('МЕХ 1-22', views.MEX_1_22),
    path('МЕХ 2-22', views.MEX_2_22),
    path('ХТП 1-22', views.XTP_1_22),
    path('ХТП 2-22', views.XTP_2_22),
    path('АиУ 2-22', views.AIY_2_22),
    path('ТДНГ 1-22', views.TDNG_1_22),
    path('ПО 2-22', views.PO_2_22),
    path('ХТП 3-22', views.XTP_3_22),
    path('ПО 3-22', views.PO_3_22)

]