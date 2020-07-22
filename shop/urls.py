from django.urls import path, register_converter
from shop import views

app_name = 'shop'

register_converter(FourDigitYearConverter,'yyyy')

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('shop/', views.item_list, name='item_new'),
    path('<int:id>/edit/', views.item_edit, name='item_edit'),  # Item수정
    path('<int:id>/delete/', views.item_delete, name='item_delete'),  # Item삭제
    path('<int:id>/reviews/', views.review_list, name='review_list'),  # 리뷰목록
    path('<int:item_id>/reviews/<int:id>/edit/$', views.review_edit,  # 리뷰수정
         name='review_edit'),
    path('<int:item_id>/reviews/<int:id>/delete/$', views.review_delete, name='review_delete'),
]
