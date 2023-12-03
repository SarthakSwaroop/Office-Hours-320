from .models import StudentAvailability, StudentRankings, ProfessorOptions, StudentSchedule, Login
from django.shortcuts import render, redirect
from .forms import StudentAvailabilityForm, StudentRankingsForm, StudentScheduleForm, ProfessorOptionsForm, LoginForm
from .serializers import StudentAvailabilitySerializer, StudentRankingsSerializer, StudentScheduleSerializer, ProfessorOptionsSerializer, LoginSerializer
from rest_framework import viewsets

def new_student_availability(request):
    if request.method == 'POST':
        form = StudentAvailabilityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_availability')
    else:
        form = StudentAvailabilityForm()
    return render(request, 'myapp/new_student_availability.html', {'form': form})


def student_availability(request):
    students = StudentAvailability.objects.all()
    return render(request, 'myapp/student_availability.html', {'students': students})

class StudentAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = StudentAvailability.objects.all()
    serializer_class = StudentAvailabilitySerializer

def new_student_rankings(request):
    if request.method == 'POST':
        form = StudentRankingsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_rankings')
    else:
        form = StudentRankingsForm()
    return render(request, 'myapp/new_student_rankings.html', {'form': form})


def student_rankings(request):
    students = StudentAvailability.objects.all()
    return render(request, 'myapp/student_rankings.html', {'students': students})

class StudentRankingsViewSet(viewsets.ModelViewSet):
    queryset = StudentRankings.objects.all()
    serializer_class = StudentRankingsSerializer

def new_student_schedule(request):
    if request.method == 'POST':
        form = StudentScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_schedule')
    else:
        form = StudentScheduleForm()
    return render(request, 'myapp/new_student_schedule.html', {'form': form})


def student_schedule(request):
    students = StudentSchedule.objects.all()
    return render(request, 'myapp/student_schedule.html', {'students': students})

class StudentScheduleViewSet(viewsets.ModelViewSet):
    queryset = StudentSchedule.objects.all()
    serializer_class = StudentScheduleSerializer

def new_professor_options(request):
    if request.method == 'POST':
        form = ProfessorOptionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('professor_options')
    else:
        form = ProfessorOptionsForm()
    return render(request, 'myapp/new_professor_options.html', {'form': form})


def professor_options(request):
    professor = ProfessorOptions.objects.all()
    return render(request, 'myapp/professor_options.html', {'professor': professor})

class ProfessorOptionsViewSet(viewsets.ModelViewSet):
    queryset = ProfessorOptions.objects.all()
    serializer_class = ProfessorOptionsSerializer


def new_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'myapp/login.html', {'form': form})


def login(request):
    login = login.objects.all()
    return render(request, 'myapp/login.html', {'login': login})

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer