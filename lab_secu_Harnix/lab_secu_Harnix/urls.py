from django.conf.urls.static import static
from lab_secu_Harnix import settings
from django.contrib import admin
from django.urls import path
from db_secu.views import index, profil
from accounts.views import signup, logout_user, login_user

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name="signup"),
    path('logout/', logout_user, name="logout"),
    path('login/', login_user, name="login"),
    path('profil/', profil, name="profil"),    



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
