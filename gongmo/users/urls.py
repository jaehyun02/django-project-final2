from users import views
from django.urls import path


app_name='users'
urlpatterns=[
    path('',views.opening,name='opening'),
    path('login/',views.login,name='login'),
    path('signUp/',views.signUp,name='signUp')
]
