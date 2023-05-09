from django.urls import path
from .views import URLCreateView, URLRedirectView


urlpatterns = [
    path('shrt/', URLCreateView.as_view(), name='url-create'),
    path('shrt/<str:short_url>/', URLRedirectView.as_view(), name='url-redirect'),
    path('<str:short_url>/', URLRedirectView.as_view(), name='short-url-redirect'),
]
