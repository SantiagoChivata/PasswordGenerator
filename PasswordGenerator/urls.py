from django.urls import path
from generator import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about , name='about'),
    path('recommendations/', views.recommendations , name='recommendations'),
    path('generate-password', views.password , name='password'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
