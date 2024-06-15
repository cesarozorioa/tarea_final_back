from django.urls import path
from App1.views import IndexReview,ProyectoView,actualizar_item

urlpatterns = [  
    path('actualizar-item/<int:item_id>/', actualizar_item, name='actualizar_item'), 
    path('',IndexReview),
    path('proyectos/<int:id>',ProyectoView),
]
