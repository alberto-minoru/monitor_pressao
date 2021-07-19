from django.urls import path
from .views import PressaoListView, PressaoDetailView

urlpatterns = [
    path('', PressaoListView.as_view(), name='registros_list'),
    path('<int:pk>/', PressaoDetailView.as_view(), name='registro_detail'),
]
