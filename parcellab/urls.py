from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from parcellab import settings
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('shipping.urls')),
]

schema_view = get_schema_view(
   openapi.Info(
      title="Parcel Lab",
      default_version='v1',
      description="This is Parcel Lab's Task APIs description",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns += [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]