from django.urls import path
from board import views

app_name='board'
urlpatterns = [
    path('main/',views.main,name='main'),
    path('write/',views.write,name='write'),
    path('detail/<int:boardid>/',views.detail,name='detail'),
    path('detail/<int:boardid>/delete/',views.delete,name='delete')
]