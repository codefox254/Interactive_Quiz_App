from django.contrib import admin
from .models import Quiz, Question, Answer, Profile

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1  # Number of extra forms to display

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # Number of extra forms to display

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    search_fields = ('title',)
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz', 'answer_type')
    search_fields = ('text',)

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Profile)
