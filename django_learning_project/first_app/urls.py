from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("<int:num1>/",views.course_number,name="course_number"),
    path("<str:item>/", views.course, name="course"),
    path("<int:num1>/<int:num2>/",views.multiply_view,name="multiply")   
]

#şuan urls.py ile views.py birbirine bağlandı.
#path("url de gözükecek ad",views.pydeki fonksiyon adı,name=urlye özel bir isim vermek için kullanılır)
#str item/ kısmı bize dictionary içinden eğer python anahtarı varsa değerini dönecek.