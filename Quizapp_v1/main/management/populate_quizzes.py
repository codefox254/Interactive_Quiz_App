from django.db import models
from django.contrib.auth.models import User

# Quiz Categories
CATEGORIES = [
    ('networking', 'Networking'),
    ('databases', 'Databases'),
    ('computer_security', 'Computer Security'),
    ('programming', 'Programming'),
    ('computer_systems', 'Computer Systems'),
]

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORIES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=255)
    answer_type = models.CharField(max_length=50, default='multiple_choice')  # Assuming multiple choice

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{'Correct' if self.is_correct else 'Incorrect'}: {self.text}"


class UserQuiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_quizzes')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='user_quizzes')
    score = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title}"
