from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, \
    verify_jwt_token
from django.conf import settings
from django.conf.urls.static import static

from usac.rest_api.views import DirectorView, PromoterView, EventTypeView, \
    EventDayView, RaceView, EventView, ParticipantView


rest_router = routers.DefaultRouter()
rest_router.trailing_slash = "/?"  # added to support both / and slashless
rest_router.register(r'director', DirectorView)
rest_router.register(r'promoter', PromoterView)
rest_router.register(r'event_type', EventTypeView)
rest_router.register(r'event_day', EventDayView)
rest_router.register(r'race', RaceView)
rest_router.register(r'event', EventView)
rest_router.register(r'participant', ParticipantView)

urlpatterns = [
    path('', RedirectView.as_view(url='/api/v1/')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(rest_router.urls)),
    path('token/auth/', obtain_jwt_token),
    path('token/refresh/', refresh_jwt_token),
    path('token/verify/', verify_jwt_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
