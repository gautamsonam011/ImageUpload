from django.contrib import admin
from django.urls import path
# from Image import views
from CrudOperation import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('image', views.image_upload, name='image'),
    # path('show', views.show_image, name='show'),
    # path('hotel', views.hotel_image_view, name='hotel'),
    # path('success', views.show_hotel, name='success'),
    path('index', views.index_page, name='index'),
    path('home', views.home_page, name='home'),
    # path('update-std/<int:pk>', views.update_std, name='update-std'),
    path('delete-std/<int:pk>', views.delete_std, name='delete-std'),
    path('do-update/<int:pk>', views.do_update, name='do-update'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)