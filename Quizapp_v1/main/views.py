from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Quiz, Question, Answer  # Importing Quiz, Question, and Answer models

# Home view
def home(request):
    return render(request, 'main/home.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after login
        else:
            return render(request, 'registration/login.html', {'error_message': 'Invalid credentials'})

    return render(request, 'registration/login.html')

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to the login page after signup
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})

# Logout view
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

# Quizzes Home View
@login_required
def quizzes_view(request):
    categories = ['Networking', 'Databases', 'security', 'Programming', 'systems']
    return render(request, 'main/quizzes.html', {'categories': categories})

# Quiz Category View - Filter quizzes based on category
@login_required
def quiz_category_view(request, category):
    quizzes = Quiz.objects.filter(category=category)  # Fetch quizzes based on category
    return render(request, f'main/{category.lower()}.html', {'quizzes': quizzes, 'category': category})

# Taking a specific quiz
@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()  # Assuming a quiz has a relationship with questions

    if request.method == 'POST':
        score = 0
        total_questions = len(questions)
        for question in questions:
            selected_option = request.POST.get(f'question_{question.id}')
            if selected_option and int(selected_option) == question.correct_answer.id:  # Assuming correct_answer is a ForeignKey to Answer
                score += 1

        # Redirect to the results page
        return redirect('quiz_results', quiz_id=quiz.id, score=score, total_questions=total_questions)

    return render(request, 'main/take_quiz.html', {'quiz': quiz, 'questions': questions})

# Quiz Results
@login_required
def quiz_results(request, quiz_id, score, total_questions):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    correct_answers = score
    incorrect_answers = total_questions - score
    return render(request, 'main/quiz_results.html', {
        'quiz': quiz,
        'score': correct_answers,
        'total_questions': total_questions,
        'incorrect_answers': incorrect_answers
    })

# Placeholder for creating new quizzes (admin or teacher users)
@login_required
def create_quiz(request):
    if request.method == 'POST':
        # Logic for creating and saving a quiz
        return redirect('quizzes')  # Redirect after creating a quiz

    return render(request, 'main/create_quiz.html')
