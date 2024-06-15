from django.urls import path
from App1.views import IndexReview,ProyectoView

urlpatterns = [   
    path('',IndexReview),
    path('proyectos/<int:id>',ProyectoView),
]
