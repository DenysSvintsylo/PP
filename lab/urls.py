
from django.contrib import admin
from django.urls import path, include, re_path
from main.views import MallList, MallDetail
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from main.viewsets import MallViewSet, CitylViewSet, CustomUserViewSet
from rest_framework.routers import DefaultRouter
from main.models import Mall, CustomUser, City

router = DefaultRouter()
router.register(r'malls', MallViewSet, basename='mall')
router.register(r'cities', CitylViewSet, basename='city')
router.register(r'users', CustomUserViewSet, basename='customuser')

schema_view = get_schema_view(
   openapi.Info(
      title="API Docs",
      default_version='v1',
      description="Документація для API",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
# admin.site.register(Mall)
# admin.site.register(CustomUser)
# admin.site.register(City)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('main.urls'))
]
