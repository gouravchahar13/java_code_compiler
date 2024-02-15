from django.contrib import admin
from django.urls import path
from home.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #home
    path('',home,name='home'),
    path('signup/',Signup_view,name='signup'),
    path('login/',login_page,name='login_pg'),
    #accounts
    path('logout/<str:username>',log_out),
    path('delete/<str:username>',delete_user),
    #main compiler
    path('code_compiler/',code_compiler,name='main'),
]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

