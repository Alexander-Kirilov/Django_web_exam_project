from django.contrib import admin
from django.urls import path, include

from ff_tickets.news.views import NewsListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', NewsListView.as_view(), name='index'),
    path('tickets/', include('ff_tickets.tickets.urls')),
    path('auth_app/', include('ff_tickets.auth_app.urls')),
    path('news/', include('ff_tickets.news.urls')),
    path('instructions/', include('ff_tickets.instructions.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

