
from django.contrib import admin
from django.urls import path,include
from mediapp import views
from django.contrib.auth import views as auth_views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.userLogin,name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'mediapp/logout.html') , name = 'logout'), 
    path('',views.index,name='index'),
    path('change',auth_views.PasswordChangeView.as_view(template_name = 'mediapp/change.html'),name='change'),
    path('change/done/',auth_views.PasswordChangeDoneView.as_view(template_name = 'mediapp/changed.html'),name='password_change_done'),
    path('reset/',auth_views.PasswordResetView.as_view(template_name = 'mediapp/reset.html'),name='reset'),
    path('reset/done',auth_views.PasswordResetDoneView.as_view(template_name = 'mediapp/reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name = 'mediapp/reset_confirm.html'),name='password_reset_confirm'),
    path('reset/ended/',auth_views.PasswordResetCompleteView.as_view(template_name = 'mediapp/reset_complete.html'),name = 'password_reset_complete')

]   