
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('corecode.urls')),

    path('student/', include('students.urls')),

    path('staff/', include('staffs.urls')),
    path('finance/', include('finance.urls')),
    path('result/', include('result.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


