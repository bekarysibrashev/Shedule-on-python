from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('АиУ 1-20', views.AIY_1_20),
    path('БНГС 1-20', views.BNGS_1_20),
    path('ЭС 1-20', views.ES_1_20),
    path('ЭС 2-20', views.ES_2_20),
    path('ЭС 3-20', views.ES_3_20),
    path('ЭНГМ 1-20', views.ENGM_1_20),
    path('ЭНГМ 2-20', views.ENGM_2_20),
    path('ИС 1-20', views.IS_1_20),
    path('ИС 2-20', views.IS_2_20),
    path('КИП 3-20', views.KIP_3_20),
    path('КИП 4-20', views.KIP_4_20),
    path('КИП 11-20', views.KIP_11_20),
    path('ТХИ 1-20', views.TXI_1_20),
    path('ТХИ 2-20', views.TXI_2_20),
    path('ТХИ 3-20', views.TXI_3_20),
    path('КИП 1-20', views.KIP_1_20),
    path('КИП 2-20', views.KIP_2_20),
    path('ТДНГ 1-20', views.TDNG_1_20),
    

]