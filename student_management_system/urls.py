from django.urls import path ,include


from . import views
urlpatterns = [
    path('', views.login_view, name='login'),
   
    path('students/', views.students_list, name='students'),
    path('courses/', views.courses, name='courses'),
    path('add/', views.add_student, name='add_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('register/', views.register, name='register'),
    path('homepage/', views.homepage, name='homepage'),
    path('home', views.homepage, name='home'),
    path('attendance', views.mark_attendance, name='mark_attendance'),
    path('attendance/list/', views.attendance_records, name='attendance_records'),
    path('reports/', views.reports, name='reports'),
    path('face-feed/', views.face_feed, name='face_feed'),
    path('face-attendance/', views.face_attendance, name='face_attendance'),
    path('mark/', views.mark_face_attendance, name='mark'),

    

]

