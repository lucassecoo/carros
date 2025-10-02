from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from cars.views import CarListView, NewBrandView, NewCarCreateView, CarDetailView, CarUpdateView, CarDeleteView
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name='logout'),
    path('cars/', CarListView.as_view(), name='cars_list'),
    path('new_car', NewCarCreateView.as_view(), name='new_car'),
    path('new_brand', NewBrandView.as_view(), name='new_brand'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('cars/<int:pk>/update', CarUpdateView.as_view(), name='car_update'),
    path('cars/<int:pk>/delete', CarDeleteView.as_view(), name='car_delete')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
