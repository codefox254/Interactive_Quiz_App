from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.management.base import BaseCommand


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100, default='Uncategorized')  # Define default here
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=255)
    answer_type = models.CharField(max_length=50)  # e.g., 'multiple_choice', 'true_false', etc.

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
    score = models.PositiveIntegerField(default=0)  # Changed to PositiveIntegerField for non-negative scores
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title}"


class Command(BaseCommand):
    help = 'Populate the database with sample quiz questions and answers'

    def handle(self, *args, **kwargs):
        categories = {
            'networking': [
                {
                    'question': "What does TCP stand for?",
                    'options': ["Transmission Control Protocol", "Transfer Control Protocol", "Transport Communication Protocol", "Transmission Communication Protocol"],
                    'correct': 0
                },
                {
                    'question': "Which device forwards traffic between different networks?",
                    'options': ["Router", "Switch", "Hub", "Firewall"],
                    'correct': 0
                },
                {
                    'question': "What is the standard port number for HTTP?",
                    'options': ["80", "443", "22", "8080"],
                    'correct': 0
                },
                {
                    'question': "What is the purpose of DNS?",
                    'options': ["Translate domain names to IP addresses", "Translate IP addresses to MAC addresses", "Secure data communication", "Block unauthorized traffic"],
                    'correct': 0
                },
                {
                    'question': "Which layer of the OSI model does IP operate in?",
                    'options': ["Network", "Transport", "Data Link", "Physical"],
                    'correct': 0
                },
            ],
            'databases': [
                {
                    'question': "What is a primary key in a database?",
                    'options': ["A unique identifier for a record", "A password for database access", "An index of all records", "An attribute used for sorting data"],
                    'correct': 0
                },
                {
                    'question': "Which SQL keyword is used to retrieve data from a database?",
                    'options': ["SELECT", "UPDATE", "DELETE", "INSERT"],
                    'correct': 0
                },
                {
                    'question': "What is the purpose of an index in a database?",
                    'options': ["To speed up data retrieval", "To store unique values", "To enforce data integrity", "To manage transactions"],
                    'correct': 0
                },
                {
                    'question': "Which of the following is a NoSQL database?",
                    'options': ["MongoDB", "PostgreSQL", "Oracle", "MySQL"],
                    'correct': 0
                },
                {
                    'question': "What does ACID stand for in database transactions?",
                    'options': ["Atomicity, Consistency, Isolation, Durability", "Accuracy, Consistency, Integrity, Durability", "Atomicity, Consistency, Integration, Data", "Accuracy, Clarity, Integrity, Durability"],
                    'correct': 0
                },
            ],
            'computer_security': [
                {
                    'question': "What is the main purpose of a firewall?",
                    'options': ["To block unauthorized access", "To store passwords", "To optimize network speed", "To scan emails"],
                    'correct': 0
                },
                {
                    'question': "What does SSL stand for?",
                    'options': ["Secure Sockets Layer", "Secure Software Layer", "Secure Security Layer", "Simple Sockets Layer"],
                    'correct': 0
                },
                {
                    'question': "Which of the following is a form of malware?",
                    'options': ["Virus", "Firewall", "Router", "Switch"],
                    'correct': 0
                },
                {
                    'question': "What does encryption ensure?",
                    'options': ["Confidentiality", "Availability", "Integrity", "Authenticity"],
                    'correct': 0
                },
                {
                    'question': "What is a brute-force attack?",
                    'options': ["Trying all possible password combinations", "Using social engineering techniques", "Sending multiple viruses", "Blocking a website's access"],
                    'correct': 0
                },
            ],
            'programming': [
                {
                    'question': "What does HTML stand for?",
                    'options': ["Hypertext Markup Language", "Hightext Machine Language", "Hyperlink and Text Markup Language", "High-level Text Markup Language"],
                    'correct': 0
                },
                {
                    'question': "Which language is primarily used for web development?",
                    'options': ["JavaScript", "Python", "C++", "Java"],
                    'correct': 0
                },
                {
                    'question': "What is the function of a compiler?",
                    'options': ["Converts source code into machine code", "Runs the code line by line", "Manages memory", "Allocates resources"],
                    'correct': 0
                },
                {
                    'question': "What is an API?",
                    'options': ["Application Programming Interface", "Automatic Processing Instruction", "Automatic Programming Interface", "Applied Processing Interface"],
                    'correct': 0
                },
                {
                    'question': "What is the term for a variable that is accessible in all scopes?",
                    'options': ["Global Variable", "Local Variable", "Instance Variable", "Static Variable"],
                    'correct': 0
                },
            ],
            'computer_systems': [
                {
                    'question': "What does CPU stand for?",
                    'options': ["Central Processing Unit", "Computer Personal Unit", "Central Program Unit", "Computer Processing Unit"],
                    'correct': 0
                },
                {
                    'question': "What is the main function of RAM in a computer system?",
                    'options': ["Stores data temporarily for quick access", "Stores data permanently", "Processes data", "Manages power"],
                    'correct': 0
                },
                {
                    'question': "What is an operating system?",
                    'options': ["Software that manages hardware and software resources", "A type of network protocol", "A method for storing data", "A tool for optimizing performance"],
                    'correct': 0
                },
                {
                    'question': "Which of the following is an example of an input device?",
                    'options': ["Keyboard", "Monitor", "CPU", "RAM"],
                    'correct': 0
                },
                {
                    'question': "What does BIOS stand for?",
                    'options': ["Basic Input Output System", "Binary Input Output System", "Basic Internal Operating System", "Binary Internal Operating System"],
                    'correct': 0
                },
            ],
        }

        for category, questions in categories.items():
            quiz = Quiz.objects.create(title=category.capitalize(), description=f"{category.capitalize()} quiz")

            for q in questions:
                question = Question.objects.create(quiz=quiz, text=q['question'], answer_type='multiple_choice')
                for i, option in enumerate(q['options']):
                    Answer.objects.create(question=question, text=option, is_correct=(i == q['correct']))

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample questions and answers'))


class CustomUser(AbstractUser):
    # Add additional fields here if needed
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(default="example@example.com")

    def __str__(self):
        return self.user.username
