from django.urls import path, include
from soldiers.views import about, SolderHome, AddSolder, ShowSoldier, RegisterUser, LoginUser, logout_user
from WEB import  settings
from django.conf.urls.static import static
from rest_framework import routers

from soldiers.viewsets import SolderViewSet

router = routers.DefaultRouter()
router.register(r'solders', SolderViewSet, basename='solders')

urlpatterns = [
    path('', SolderHome.as_view(), name ='home'),
    path('about/', about, name='about'),
    path('solder/<slug:so_slug>/', ShowSoldier.as_view(), name='solder'),
    path('addsolder/', AddSolder.as_view(), name='addsolder'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('api/v1/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)