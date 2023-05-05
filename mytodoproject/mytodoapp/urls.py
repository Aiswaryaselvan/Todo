from django.urls import path
from.import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id1>/', views.Update, name='update'),
    path('listview/',views.Listview.as_view(),name='listview'),
    path('detailview/<int:pk>/',views.Detailview.as_view(),name='detailview'),
    path('detailview/<int:pk>/',views.UpdateView.as_view(),name='updateview'),
    path('deleteview/<int:pk>/',views.Deleteview.as_view(),name='Deleteview'),
]