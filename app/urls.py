from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views 
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetDoneView,PasswordResetCompleteView
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
urlpatterns = [
    path('home/',views.home,name='home'),
    path("jump/<id>",views.jump,name='jump'),
    path('register/',views.Registration,name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='home'),name='logout'),
    path('profile/',views.profile,name='profile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('password_change/',PasswordChangeView.as_view(template_name='registration/password_change.html'),name='password_change'),
    path('password_change_done/',PasswordChangeDoneView.as_view(template_name='registration/password_changed.html'),name='password_change_done'),
    path('password_reset/',PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='registration/password_reset_set.html'),name='password_reset_confirm'),
    path("password_reset/done",PasswordResetDoneView.as_view(template_name='registration/password_reset_done_alert.html'),name='password_reset_done'),
    path('password_reset/complete',PasswordResetCompleteView.as_view(template_name='registration/password_reset_completed.html'),name='password_reset_complete'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.About,name='about'),
    path('delete/<id>',views.delete,name='delete'),
    path('update/<id>',views.update,name='update'),
    path('search/',views.searchbar,name='search'),

]
    


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)