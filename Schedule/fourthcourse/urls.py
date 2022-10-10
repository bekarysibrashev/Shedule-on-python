from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('АиУ 1-19', views.AIY_1_19),
    path('АиУ 2-19', views.AIY_2_19),
    path('БНГС 1-19', views.BNGS_1_19),
    path('ЭС 1-19', views.ES_1_19),
    path('ЭС 2-19', views.ES_2_19),
    path('ЭС 3-19', views.ES_3_19),
    path('ЭС 4-19', views.ES_4_19),
    path('ЭНГМ 1-19', views.ENGM_1_19),
    path('ЭНГМ 2-19', views.ENGM_2_19),
    path('ЭНГМ 3-19', views.ENGM_3_19),
    path('ИС 1-19', views.IS_1_19),
    path('ИС 2-19', views.IS_2_19),
    path('КИП 1-19', views.KIP_1_19),
    path('КИП 2-19', views.KIP_2_19),
    path('КИП 3-19', views.KIP_3_19),
    path('КИП 4-19', views.KIP_4_19),
    path('ТДНГ 1-19', views.TDNG_1_19),
    path('ТХИ 1-19', views.TXI_1_19),
    path('ТХИ 2-19', views.TXI_2_19),
    path('ТХИ 3-19', views.TXI_3_19)

]