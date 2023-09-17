from django.urls import path
from . import views

app_name = 'App_login'

urlpatterns = [
    path('sign_up/',views.sign_up, name='signup'),
    path('login/',views.login_page, name='login'),
    path('logut/',views.logout_user, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('change/',views.user_change, name='change'),
    path('password/',views.pass_change, name='password'),
    path('add-picture/',views.add_profile_pic, name='add_pro_pic'),
    path('change-picture/',views.change_pro_pic, name='change_pro_pic'),

]

