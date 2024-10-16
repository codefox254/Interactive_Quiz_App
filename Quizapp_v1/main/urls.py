# urls.py

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's built-in auth URLs
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/signup/', views.signup, name='signup'),

    # URLs for specific quiz categories
    path('quizzes/networking/', views.quiz_category_view, {'category': 'Networking'}, name='networking_quiz'),
    path('quizzes/databases/', views.quiz_category_view, {'category': 'Databases'}, name='databases_quiz'),
    path('quizzes/security/', views.quiz_category_view, {'category': 'Computer Security'}, name='security_quiz'),
    path('quizzes/programming/', views.quiz_category_view, {'category': 'Programming'}, name='programming_quiz'),
    path('quizzes/systems/', views.quiz_category_view, {'category': 'Computer Systems'}, name='systems_quiz'),

    # Quiz URLs
    path('quizzes/', views.quizzes_view, name='quizzes'),
    path('quizzes/<str:category>/', views.quiz_category_view, name='quiz_category'),
    path('quizzes/take/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
    path('quizzes/results/<int:quiz_id>/<int:score>/<int:total_questions>/', views.quiz_results, name='quiz_results'),
    path('quizzes/create/', views.create_quiz, name='create_quiz'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
