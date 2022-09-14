from django.contrib import admin
from django.urls import path,re_path
from App import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.home),
    re_path(r'^register$',views.signup),
    re_path(r'^login/',views.login),
    re_path(r'^form/',views.book_form),
    re_path(r'^list/',views.book_list),
    path('',views.book_form,name='book_insert'),
    path('<int:id>/',views.book_form,name='book_update'),
    path('list/',views.book_list,name='book_list'),
    path('delete<int:id>/',views.book_delete,name='book_delete'),

]