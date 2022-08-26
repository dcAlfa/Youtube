from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from youtubeapp.views import *
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Bu loyha Youtube uchun klon qilib ishlatilaishi mumkin",
      contact=openapi.Contact(email="Muhammadjonov Muhammadali: <Bekruhblog@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-doc'),
    path('accountlar/', AccountCreate.as_view()),
    path('account/<int:pk>/', AccountRD.as_view()),
    path('vediolar/', VedioCreate.as_view()),
    path('vedio/<int:pk>/', VedioRD.as_view()),
    path('pleylistlar/', PleylistCreate.as_view()),
    path('pleylist/<int:pk>/', PleylistRD.as_view()),
    path('obunalar/', ObunaCreate.as_view()),
    path('obuna/<int:pk>/', ObunaRD.as_view()),
    path('likelar/', LikeCreate.as_view()),
    path('like/<int:pk>/', LikeRD.as_view()),
    path('historylar/', HistoryCreate.as_view()),
    path('history/<int:pk>/', HistoryRD.as_view()),
]
