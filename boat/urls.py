from django.urls import path

from boat.apps import BoatConfig
from boat.views import BoatListView, BoatDetailView

app_name = BoatConfig.name


urlpatterns = [
    path('', BoatListView.as_view(), name='boat_list'),
    path('<int:pk>/', BoatDetailView.as_view(), name='boat_view'),
    # path('blog/view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    # path('blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='edit_blog'),
    # path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),

]