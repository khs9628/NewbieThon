from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name='index'),
    path('aicohol/', views.aicohol, name= "aicohol"),
    path('health/', views.health, name = "health"),

    path('<int:donkey_id>/', views.detail_home,name="detail_home"),
    path('health/<int:health_id>/',views.detail_health,name="detail_health"),
    path('aicohol/<int:aicohol_id>/',views.detail_aicohol,name="detail_aicohol"),
    
    path('about/', views.about , name = 'about'),
    path('mypage/', views.mypage , name = 'mypage'),
    path('medicine/', views.medicine , name = 'medicine'),
    path('recipe/', views.recipe , name = 'recipe'),

    path('login/', views.login, name="login"),
    path('signin/', views.signin, name="signin"),

    path('new_home',views.new_home, name = "new_home"),
    path('health/new_health', views.new_health, name = "new_health"),
    path('aicohol/new_aicohol', views.new_aicohol, name = "new_aicohol"),

    path('create_home', views.create_home, name = "create_home"),
    path('health/create_health', views.create_health, name = "create_health"),
    path('aicohol/create_aicohol', views.create_aicohol, name = "create_aicohol"),
]