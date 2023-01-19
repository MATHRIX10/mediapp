
from django.contrib import admin
from django.urls import path,include
from mediapp import views
from django.contrib.auth import views as auth_views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.userLogin,name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'mediapp/logout.html') , name = 'logout'), 
    path('',views.index,name='index'),
    path('reset',auth_views.PasswordChangeView.as_view(template_name = 'mediapp/reset.html'),name='reset'),
    path('reset/done/',auth_views.PasswordChangeDoneView.as_view(template_name = 'mediapp/changed.html'),name='password_change_done'),
]   