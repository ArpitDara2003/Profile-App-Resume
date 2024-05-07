from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name = 'home'),
    path('home',views.home,name = 'home'),
    path('allskills', views.allskills, name = 'allskills'),
    path('certificates',views.certificates, name = 'certificates'),
    path('logout', views.logout, name = 'logout'),
    path('login',views.login, name = 'login'),
    path('profile',views.profile, name = 'profile'),
    path('register', views.register, name = 'register'),
    path('addskill',views.addskill, name = 'addskill'),
    path('addcertificate',views.addcertificate, name = 'addcertificate'),
    path('skill', views.skill, name='skill'),
    path('certificate', views.certificate, name='certificate'),    
    path('delete_skill',views.delete_skill, name = 'delete_skill'),
    path('editskill', views.editskill, name = 'editskill'),
    path('deletecertificate',views.deletecertificate, name = 'deletecertificate'),
    path('editcertificate', views.editcertificate, name = 'editcertificate'),
    path('saveskill',views.saveskill, name = 'saveskill'),
    path('savecertificate',views.savecertificate, name = 'savecertificate'),
    path('editprofile', views.editprofile, name='editprofile'),
    path('saveprofile',views.saveprofile, name = 'saveprofile'),
    path('changepassword',views.changepassword, name = 'changepassword'),
    path('changeusername',views.changeusername, name = 'changeusername'),
    path('certificate', views.certificate, name='certificate'),


    path('<str:username>', views.home_of, name='home_of'),
    path('<str:username>/home', views.home_of, name='home_of'),
    path('<str:username>/allskills', views.allskills_of, name='allskills_of'),
    path('<str:username>/skill', views.skill_of, name='skill_of'),
    path('<str:username>/certificates', views.certificates_of, name='certificates_of'),
    path('<str:username>/certificate', views.certificate_of, name='certificate_of'),
    
    path('<str:username>/logout', views.logout, name='logout_of'),
    path('<str:username>/profile', views.profile, name='profile_of'),
    path('<str:username>/addskill', views.addskill, name='addskill_of'),
    path('<str:username>/addcertificate',views.addcertificate, name = 'addcertificate_of'),
    path('<str:username>/delete_skill',views.delete_skill, name = 'delete_skill_of'),
    path('<str:username>/editskill', views.editskill, name = 'editskill_of'),
    path('<str:username>/deletecertificate',views.deletecertificate, name = 'deletecertificate_of'),
    path('<str:username>/editcertificate', views.editcertificate, name = 'editcertificate_of'),
    path('<str:username>/saveskill',views.saveskill, name = 'saveskill_of'),
    path('<str:username>/savecertificate',views.savecertificate, name = 'savecertificate_of'),
    path('<str:username>/editprofile', views.editprofile, name='editprofile_of'),
    path('<str:username>/saveprofile',views.saveprofile, name = 'saveprofile_of'),
    path('<str:username>/changepassword',views.changepassword, name = 'changepassword_of'),
    path('<str:username>/changeusername',views.changeusername, name = 'changeusername_of'),

    
]

