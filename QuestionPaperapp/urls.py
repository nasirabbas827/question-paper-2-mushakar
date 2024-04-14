from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views

urlpatterns = [
    path('', views.login, name='login'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.student_signup, name='signup'),
    path('view_exams/<int:course_id>/', views.view_exams, name='view_exams'),
    path('view_difficulty_levels/<int:exam_id>/', views.view_difficulty_levels, name='view_difficulty_levels'),
    path('view_questions_by_difficulty/<int:exam_id>/<str:difficulty>/', views.view_questions_by_difficulty, name='view_questions_by_difficulty'),
    path('submit_paper/<int:exam_id>/', views.submit_paper, name='submit_paper'),
    path('view_marks/', views.view_marks, name='view_marks'),
    path('view_notifications/', views.view_notifications, name='view_notifications'),

]




# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
