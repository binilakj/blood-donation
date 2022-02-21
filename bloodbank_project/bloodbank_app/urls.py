from django.urls import path, include
from . import views


app_name="bloodbank_app"

urlpatterns = [


path('', views.index, name='index'),
path('about',views.about,name='about'),
path('services',views.services,name='services'),
path('register', views.register, name='register'),
path('login', views.login, name='login'),
path('registerations',views.registerations,name='registerations'),
path('<slug:c_slug>/',views.registerations,name='center_category'),
path('wayanad', views.wayanad, name='wayanad'),
path('thrissur',views.thrissur,name='thrissur'),
path('ernakulam',views.ernakulam,name='ernakulam'),
path('idukki',views.idukki,name='idukki'),
path('alappuzha',views.alappuzha,name='alappuzha'),
path('kannur',views.kannur,name='kannur'),
path('kasargod',views.kasargod,name='kasargod'),
path('kollam',views.kollam,name='kollam'),
path('kottayam',views.kottayam,name='kottayam'),
path('kozhikode',views.kozhikode,name='kozhikode'),
path('malappuram',views.malappuram,name='malappuram'),
path('palakkad',views.palakkad,name='palakkad'),
path('pathanamthitta',views.pathanamthitta,name='pathanamthitta'),
path('thiruvananthapuram',views.thiruvananthapuram,name='thiruvananthapuram'),
path('button',views.button,name='button'),
path('message',views.message,name='message'),

]
