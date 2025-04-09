from django.urls import path, include
from uiia.views import vista_principal, vista_crear, vista_generar, vista_regenerar, vista_eliminar, generar_componente, vista_landing

urlpatterns = [
    path('', vista_landing ,name="landing"),
    path('listado/', vista_principal, name="listado"),
    path('crear/', vista_crear, name="crear_componente"),
    path('generar/<int:id>', vista_generar, name="generar_componente"),
    path('regenerar/<int:id>', vista_regenerar, name="regenerar_componente"),
    path('eliminar/<int:id>/', vista_eliminar, name='eliminar_componente'),
]

