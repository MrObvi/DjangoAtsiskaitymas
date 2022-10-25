from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('projektai/',views.projektai, name="projektai"),
    path('projektai/<int:projektas_id>', views.projektasView, name="projektas"),
    path('register/', views.register, name='register'),
    path('user-project/', views.UserProjektasListView.as_view(), name='user-projektai'),
    path('user-project/<int:pk>/update', views.UserProjektasUpdateView.as_view(), name='user-projektai-update'),
    path('user-project/<int:pk>/delete', views.UserProjectDeleteView.as_view(), name='user-projektai-delete'),
    path('tinymce/', include('tinymce.urls')),
    path('search/', views.search, name='search'),
    # Adding social auth path
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("login/", views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("add-listing/", views.addlisting, name="add-listing"),
    path('i18n/', include('django.conf.urls.i18n')),

]
