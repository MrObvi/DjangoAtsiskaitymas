from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('projektai/',views.projektai, name="projektai"),
    path('register/', views.register, name='register'),
    path('user-project/', views.UserProjektasListView.as_view(), name='user-projektai')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
