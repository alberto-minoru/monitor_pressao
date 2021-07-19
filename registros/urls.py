from django.urls import path
from .views import PressaoListView, PressaoDetailView, PressaoCreateView, PressaoUpdateView, PressaoDeleteView

urlpatterns = [
    path('', PressaoListView.as_view(), name='registros_list'),
    path('<int:pk>/', PressaoDetailView.as_view(), name='registro_detail'),
    path('new/', PressaoCreateView.as_view(), name='registro_new'),
    path('<int:pk>/edit/', PressaoUpdateView.as_view(), name='registro_edit'),
    path('<int:pk>/delete/', PressaoDeleteView.as_view(), name='registro_delete'),
]
