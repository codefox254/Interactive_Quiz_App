from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Quiz, Question, Answer, Profile

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['quiz', 'text', 'answer_type']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['question', 'text', 'is_correct']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match")

        return cleaned_data
